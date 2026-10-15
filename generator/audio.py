import numpy as np, sys, json
from scipy.io import wavfile
SR=44100
DUR=float(sys.argv[1]) if len(sys.argv)>1 else 25.0
EV=json.load(open(sys.argv[2])) if len(sys.argv)>2 else None
N=int(SR*DUR)
music=np.zeros(N); sfx=np.zeros(N)
SEED=int(sys.argv[4]) if len(sys.argv)>4 else 7
rng=np.random.default_rng(SEED)
def t_(d): return np.arange(int(SR*d))/SR
def add(buf,start,sig,g=1.0):
    i=int(start*SR)
    if i>=len(buf): return
    j=min(len(buf),i+len(sig)); buf[i:j]+=sig[:j-i]*g
def env(n,a=0.005,r=0.3):
    t=np.arange(n)/SR; e=np.minimum(1,t/a)*np.exp(-t/r); return e
def f(n): return 440*2**((n-69)/12)
def pluck(note,d=0.5,r=0.25):
    t=t_(d); fr=f(note)
    s=np.sin(2*np.pi*fr*t)+0.35*np.sin(2*np.pi*2*fr*t)+0.12*np.sin(2*np.pi*3*fr*t)
    return s*env(len(t),0.004,r)
def bass(note,d=0.5):
    t=t_(d); fr=f(note)
    s=np.sin(2*np.pi*fr*t)+0.25*np.sin(2*np.pi*2*fr*t)
    return s*env(len(t),0.01,0.35)
def hat(d=0.06):
    n=int(SR*d); s=rng.standard_normal(n); s=np.diff(np.concatenate([[0],s]))
    return s*env(n,0.001,0.02)
def kick():
    t=t_(0.25); fr=110*np.exp(-t*18)+45
    return np.sin(2*np.pi*np.cumsum(fr)/SR)*env(len(t),0.002,0.12)
# ---- musique moderne : pop chill, 104 bpm, La m - Fa - Do - Sol
from scipy.signal import butter, lfilter, fftconvolve
def lp(x,fc,o=2): bb,aa=butter(o,fc/(SR/2)); return lfilter(bb,aa,x)
def hp(x,fc,o=2): bb,aa=butter(o,fc/(SR/2),'high'); return lfilter(bb,aa,x)
def saw(fr,t): return 2*((fr*t)%1)-1
PROGS=[[(45,[57,60,64,69]),(41,[53,57,60,65]),(48,[55,60,64,67]),(43,[55,59,62,67])],
 [(48,[55,60,64,67]),(43,[55,59,62,67]),(45,[57,60,64,69]),(41,[53,57,60,65])],
 [(41,[53,57,60,65]),(43,[55,59,62,67]),(45,[57,60,64,69]),(48,[55,60,64,67])],
 [(45,[57,60,64,69]),(43,[55,59,62,67]),(41,[53,57,60,65]),(43,[55,59,62,67])]]
TR=[0,2,-2,3,-3,5][SEED%6]
prog=[(r+TR,[n+TR for n in c]) for r,c in PROGS[SEED%4]]
bpm=[104,100,108,102,106][SEED%5]; beat=60/bpm; bar=4*beat
pad=np.zeros(N); bus=np.zeros(N); drums=np.zeros(N)
def padchord(notes,d):
    t=t_(d); s=np.zeros(len(t))
    for n in notes:
        for det in (-0.12,0,0.12): s+=saw(f(n)*2**(det/12),t+rng.random())
    s=lp(s,1800); e=np.minimum(1,t/0.25)*np.minimum(1,(d-t)/0.2); return s*e/len(notes)/3
def keys(n,d=0.5):
    t=t_(d); fr=f(n)
    s=saw(fr,t)+saw(fr*1.003,t); s=lp(s,2600)
    return s*env(len(t),0.003,0.22)*0.5
def sub(n,d):
    t=t_(d); fr=f(n); s=np.sin(2*np.pi*fr*t); s=np.tanh(2*s)*0.6+0.4*np.sin(2*np.pi*fr*t)
    e=np.minimum(1,t/0.01)*np.minimum(1,np.maximum(0,(d-t))/0.05); return s*e
def kick2():
    t=t_(0.35); fr=150*np.exp(-t*25)+48
    s=np.sin(2*np.pi*np.cumsum(fr)/SR); return s*np.minimum(1,t/0.004)*np.exp(-t/0.16)
def clap():
    n=int(SR*0.25); s=rng.standard_normal(n); s=hp(lp(s,3500),900)
    t=np.arange(n)/SR; e=np.zeros(n)
    for o in (0,0.011,0.022): e+=np.where(t>=o,np.exp(-(t-o)/0.012),0)*0.5
    e+=np.where(t>=0.03,np.exp(-(t-0.03)/0.09),0); return s*e
def shaker():
    n=int(SR*0.09); s=hp(rng.standard_normal(n),6000)
    t=np.arange(n)/SR; return s*np.sin(np.pi*np.minimum(1,t/0.09))**2
tt=0.0;b=0
side=np.ones(N)
while tt<DUR+bar:
    root,ch=prog[b%4]
    add(pad,tt,padchord(ch,bar),0.5)
    for q in range(4):
        add(bus,tt+q*beat,sub(root-12 if root>44 else root,beat*0.9),0.55)
        add(drums,tt+q*beat,kick2(),0.9)
        i=int((tt+q*beat)*SR); L=int(0.22*SR)
        if i<N: j=min(N,i+L); side[i:j]=np.minimum(side[i:j],0.35+0.65*np.linspace(0,1,j-i)**0.6)
        if q in (1,3): add(drums,tt+q*beat,clap(),0.35)
        for e8 in (0,1):
            sw=0.0 if e8==0 else 0.06*beat
            add(drums,tt+q*beat+e8*beat/2+sw,shaker(),0.06 if e8 else 0.035)
    if b>=1:
        pat=[[0,2,3,2,1],[3,2,0,1,2],[1,3,2,0,3]][SEED%3]
        rhythm=[[0,1.5,2,3,3.5],[0,0.5,1.5,2.5,3],[0,1,1.5,2.5,3.5]][SEED%3]
        for k,r in enumerate(rhythm): add(bus,tt+r*beat,keys(ch[pat[k]]+12,0.6),0.32)
    if b>=2 and b%2==0:
        mel=[(0,ch[3]+12),(0.75,ch[2]+12),(1.5,ch[3]+12),(2.5,ch[1]+24),(3,ch[3]+12)]
        for r,m in mel: add(bus,tt+bar+r*beat,keys(m,0.5),0.18) if False else add(bus,tt+r*beat+bar*0,keys(m+0,0.5),0.0)
    tt+=bar;b+=1
pad*=side; bus[:]=bus*(0.6+0.4*side)
ir_t=np.arange(int(SR*1.6))/SR; ir=rng.standard_normal(len(ir_t))*np.exp(-ir_t/0.45); ir=lp(ir,5000); ir/=np.sqrt(np.sum(ir**2))
wet=fftconvolve(pad*0.6+bus,ir)[:N]*0.25
music=pad*0.55+bus+drums*0.8+wet
# fondu entrée / sortie
fi=int(0.4*SR);fo=int(1.5*SR)
music[:fi]*=np.linspace(0,1,fi);music[-fo:]*=np.linspace(1,0,fo)
# ---- bruitages
def pop(p=900):
    t=t_(0.12); fr=p*np.exp(-t*12)+p*0.6
    return np.sin(2*np.pi*np.cumsum(fr)/SR)*env(len(t),0.002,0.04)
def click():
    n=int(SR*0.035); s=rng.standard_normal(n)*env(n,0.0005,0.006)
    t=np.arange(n)/SR; s+=0.6*np.sin(2*np.pi*2400*t)*env(n,0.0005,0.008); return s
def ting(note=88):
    t=t_(0.9); fr=f(note)
    s=np.sin(2*np.pi*fr*t)+0.4*np.sin(2*np.pi*2.76*fr*t)+0.2*np.sin(2*np.pi*5.4*fr*t)
    return s*env(len(t),0.002,0.25)
def whoosh(d=0.45):
    n=int(SR*d); s=rng.standard_normal(n)
    from scipy.signal import lfilter
    s=lfilter([1],[1,-0.97],s); s/=np.max(np.abs(s))
    e=np.sin(np.pi*np.linspace(0,1,n))**2; return s*e
def tada():
    out=np.zeros(int(SR*1.2))
    for k,n in enumerate([72,76,79,84]):
        s=pluck(n,0.9,0.35); i=int(k*0.08*SR); out[i:i+len(s)]+=s[:len(out)-i]
    return out
E=EV if EV else {}
for x in E.get('pop',[]): add(sfx,x[0],pop(x[1] if len(x)>1 else 900),0.5)
for x in E.get('click',[]): add(sfx,x,click(),0.35)
for x in E.get('ting',[]): add(sfx,x,ting(),0.28)
for x in E.get('whoosh',[]): add(sfx,x,whoosh(),0.22)
for x in E.get('tada',[]): add(sfx,x,tada(),0.35)
for x in E.get('chime',[]):
    for k,n in enumerate([84,88,91,96]): add(sfx,x+k*0.11,ting(n),0.2)
mix=music*0.55+sfx
mix/=max(1e-9,np.max(np.abs(mix)))/0.89
st=np.stack([mix,mix],1)
wavfile.write(sys.argv[3],SR,(st*32767).astype(np.int16))
print('ok')

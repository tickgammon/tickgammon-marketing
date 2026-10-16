import json,subprocess,numpy as np,re,sys
LANG=sys.argv[1] if len(sys.argv)>1 else 'fr'; SUF='' if LANG=='fr' else '_'+LANG
from scipy.io import wavfile
SR=44100
A=json.load(open(f'align{SUF}.json'))
L=[l.split('|',2) for l in open(f'passages_{LANG}.txt',encoding='utf8').read().strip().split('\n')]
ch={p:int(c) for p,c,t in L}; txt={p:t for p,c,t in L}
src={}
for b in ('bloc1'+SUF,'bloc2'+SUF,'bloc3'+SUF):
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',b+'.mp3','-ac','1','-ar',str(SR),b+'.wav'])
    src[b]=wavfile.read(b+'.wav')[1].astype(np.float32)/32768
LEAD=1.2; GAP=0.45; CHGAP=2.2; TAIL=4.5
out=[]; t=LEAD; tl=[]; prev=None
for a in A:
    p=a['p']
    if prev is not None:
        t+= CHGAP if ch[p]!=ch[prev] else GAP
    s=max(0,a['start']-0.04); e=a['end']+0.06
    seg=src[a['bloc']][int(s*SR):int(e*SR)]
    tl.append(dict(p=p,ch=ch[p],t0=round(t,3),d=round(len(seg)/SR,3),txt=re.sub(r'\s*\[.*?\]','',txt[p])))
    out.append((t,seg)); t+=len(seg)/SR; prev=p
total=t+TAIL
N=int(total*SR); v=np.zeros(N,np.float32)
for st,seg in out:
    i=int(st*SR); v[i:i+len(seg)]+=seg
wavfile.write(f'voice{SUF}.wav',SR,(np.clip(v,-1,1)*32767).astype(np.int16))
# enveloppe 30 fps
fps=30; n=int(total*fps); env=[]
for k in range(n):
    i=int(k/fps*SR); w=v[i:i+SR//fps]
    env.append(float(np.sqrt(np.mean(w**2))) if len(w) else 0)
m=max(env); env=[round(min(1,x/m*1.6),3) for x in env]
json.dump(dict(total=round(total,3),tl=tl,env=env),open(f'timeline{SUF}.json','w'),ensure_ascii=False)
print(total, len(tl))

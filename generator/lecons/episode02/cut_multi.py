# Leçon 2 — une seule vidéo, 3 voix : minutage commun (durée max de chaque passage sur FR/EN/ES)
import json,subprocess,numpy as np,re
from scipy.io import wavfile
SR=44100; LS=['fr','en','es']
LEAD=1.2; GAP=0.45; CHGAP=2.2; TAIL=4.5
segs={};txt={};ch={}
for L in LS:
    SUF='' if L=='fr' else '_'+L
    A=json.load(open(f'align{SUF}.json'))
    rows=[l.split('|',2) for l in open(f'passages_{L}.txt',encoding='utf8').read().strip().split('\n')]
    txt[L]={p:re.sub(r'\s*\[.*?\]','',t) for p,c,t in rows}; ch.update({p:int(c) for p,c,t in rows})
    src={}
    for b in ('bloc1'+SUF,'bloc2'+SUF,'bloc3'+SUF):
        subprocess.run(['ffmpeg','-loglevel','error','-y','-i',b+'.mp3','-ac','1','-ar',str(SR),b+'.wav'])
        src[b]=wavfile.read(b+'.wav')[1].astype(np.float32)/32768
    for a in A:
        s=max(0,a['start']-0.04); e=a['end']+0.06
        segs.setdefault(a['p'],{})[L]=src[a['bloc']][int(s*SR):int(e*SR)]
P=sorted(segs)
t=LEAD; tl={L:[] for L in LS}; com=[]; prev=None
for p in P:
    if prev is not None: t+=CHGAP if ch[p]!=ch[prev] else GAP
    D=max(len(segs[p][L]) for L in LS)/SR
    com.append(dict(p=p,ch=ch[p],t0=round(t,3),d=round(D,3),txt=txt['fr'][p]))
    for L in LS: tl[L].append(dict(p=p,ch=ch[p],t0=round(t,3),d=round(len(segs[p][L])/SR,3),txt=txt[L][p]))
    t+=D; prev=p
total=t+TAIL; N=int(total*SR); fps=30
envs={}
for L in LS:
    v=np.zeros(N,np.float32)
    for x in tl[L]:
        sg=segs[x['p']][L]; i=int(x['t0']*SR); v[i:i+len(sg)]+=sg
    wavfile.write(f'voice_{L}.wav',SR,(np.clip(v,-1,1)*32767).astype(np.int16))
    env=[]
    for k in range(int(total*fps)):
        i=int(k/fps*SR); w=v[i:i+SR//fps]; env.append(float(np.sqrt(np.mean(w**2))) if len(w) else 0)
    m=max(env); envs[L]=[round(min(1,x/m*1.6),3) for x in env]
    json.dump(dict(total=round(total,3),tl=tl[L],env=envs[L]),open(f'timeline_{L}.json','w'),ensure_ascii=False)
json.dump(dict(total=round(total,3),tl=com,env=envs['fr']),open('timeline.json','w'),ensure_ascii=False)
print(round(total,2),len(com))

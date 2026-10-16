import subprocess,re,json,sys
L=[l.split('|',2) for l in open('passages_fr.txt',encoding='utf8').read().strip().split('\n')]
groups={'bloc1':'0123','bloc2':'456','bloc3':'789'}
res=[]
for b,chs in groups.items():
    P=[(p,t) for p,c,t in L if c in chs]
    out=subprocess.run(['ffmpeg','-hide_banner','-i',b+'.mp3','-af','silencedetect=n=-40dB:d=0.15','-f','null','-'],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',out)]
    en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',out)]
    dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',b+'.mp3'],capture_output=True,text=True).stdout)
    sil=[(s,e) for s,e in zip(st,en) if s>0.05 and e<dur-0.05]
    # speech start/end
    s0=en[0] if st and st[0]<0.05 else 0
    s1=st[-1] if len(en)<len(st) or (en and en[-1]>=dur-0.05) else dur
    w=[len(re.sub(r'\[.*?\]','',t))+(25 if '[laughs]' in t else 0) for _,t in P]
    n=len(P); C=sil; m=len(C)
    tot=sum(w); k=(s1-s0)/tot
    INF=1e18
    # dp[i][j]: first i passages end at candidate j
    import math
    def cost(a,bnd,i):
        d=bnd-a; e=w[i]*k
        return (d-e)**2/e
    dp=[[INF]*(m+1) for _ in range(n)]; bk=[[None]*(m+1) for _ in range(n)]
    for j in range(m):
        dp[0][j]=cost(s0,C[j][0],0)-3*(C[j][1]-C[j][0])
    for i in range(1,n-1):
        for j in range(m):
            best=INF;bj=None
            for q in range(j):
                v=dp[i-1][q]+cost(C[q][1],C[j][0],i)-3*(C[j][1]-C[j][0])
                if v<best:best=v;bj=q
            dp[i][j]=best;bk[i][j]=bj
    best=INF;bj=None
    for q in range(m):
        v=dp[n-2][q]+cost(C[q][1],s1,n-1)
        if v<best:best=v;bj=q
    idx=[bj]; 
    for i in range(n-2,0,-1): idx.append(bk[i][idx[-1]])
    idx=idx[::-1]
    bounds=[s0]+[None]*0
    segs=[];a=s0
    for i in range(n):
        e=C[idx[i]][0] if i<n-1 else s1
        segs.append((P[i][0],round(a,3),round(e,3),round(w[i]*k,2)))
        if i<n-1:a=C[idx[i]][1]
    for s in segs: print(b,s, round(s[2]-s[1],2))
    res+= [dict(p=s[0],bloc=b,start=s[1],end=s[2]) for s in segs]
json.dump(res,open('align.json','w'),indent=1)

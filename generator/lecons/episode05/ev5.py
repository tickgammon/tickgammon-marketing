import json
d=json.load(open('timeline.json'));tl=d['tl'];T={x['p']:x for x in tl}
raw=json.load(open('evt_raw.json'))
ev={"pop":[],"click":[],"ting":[],"whoosh":[],"tada":[],"chime":[]}
def dedup(xs,g=.15):
    out=[]
    for x in xs:
        if not out or x-out[-1]>g: out.append(x)
    return out
pops=sorted({float(k.split('|')[1]) for k in raw if k.startswith('pop')})
rolls=sorted({float(k.split('|')[1]) for k in raw if k.startswith('roll')})
for x in dedup(pops): ev['pop'].append([round(x,2),700])
for r in dedup(rolls,.5):
    for j in range(7): ev['click'].append(round(r+j*.1,2))
for a,b in zip(tl,tl[1:]):
    if a['ch']!=b['ch']: ev['whoosh'].append(round(a['t0']+a['d']+.15,2))
at=lambda p,x: round(T[p]['t0']+x,2)
D=lambda p:T[p]['d']
for p in ('P02','P13'):
    for j in range(9): ev['click'].append(at(p,.3+j*.12))
# grille qui se remplit (P03) : petits pops
n=36
for k in range(0,36,3): ev['pop'].append([at('P03',.4+(D('P03')*.8-.4)*k/36),900])
for p,f in [('P04',.3),('P04',.55),('P04',.7),('P05',.35),('P05',.6),('P06',.3),('P06',.5),('P10',.3),('P11',.7),('P12',.2),('P14',.6),('P15',.55),('P16',.2),('P17',.2),('P18',.55),('P20',.3),('P22',.3),('P26',.3),('P26',.75),('P26',1.2),('P27',.3),('P27',.4),('P30',.2),('P30',.4),('P31',.3),('P33',.1)]:
    ev['pop'].append([at(p,D(p)*f if f<1 else f),500])
for p in range(4): ev['pop'].append([at('P34',D('P34')*.15+p*min(1.6,D('P34')*.75/4)+.35),800])
for p in ('P09','P12','P17','P20','P24'): ev['ting'].append(at(p,D(p)*.6))
k9=[i for i,x in enumerate(tl) if x['ch']==9][0];pv=tl[k9-1]
ev['tada']+=[at('P01',1.6),round(pv['t0']+pv['d']+.3,2),at('P34',D('P34')*.85)]
ev['chime'].append(at('P35',.5)); ev['tada'].append(at('P35',D('P35')-1.5))
json.dump(ev,open('ev.json','w'))
print({k:len(v) for k,v in ev.items()}, d['total'])

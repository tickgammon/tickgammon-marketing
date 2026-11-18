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
# (passage, instant, 1 = fraction de la durée)
P=[('P02',.15,1),('P02',.27,1),('P02',.39,1),('P02',.51,1),('P03',.3,0),('P04',.2,0),('P05',.2,0),('P06',.2,0),('P06',.45,1),('P08',.6,1),
 ('P10',.55,1),('P11',.35,1),('P13',.2,0),('P14',.15,1),('P14',.55,1),('P15',.45,1),('P16',.2,0),('P17',.2,0),('P18',.2,0),('P18',.75,1),('P19',.55,1),
 ('P20',.2,1),('P20',.6,1),('P21',.2,0),('P21',.4,1),('P22',.3,0),('P22',.55,1),('P23',.2,0),('P23',.35,1),('P24',.2,0),('P24',.3,1),('P24',.55,1),
 ('P25',.2,0),('P25',.4,1),('P25',.65,1),('P26',.6,1),('P27',.15,1),('P27',.2,0),('P27',.3,1),('P29',.2,0),('P29',.35,1),('P31',.2,0),('P32',.2,0),('P32',.5,0),('P32',.8,0),('P32',.5,1)]
for p,f,fr in P: ev['pop'].append([at(p,D(p)*f if fr else f),500])
for k in range(4): ev['pop'].append([at('P28',D('P28')*.12+k*min(1.6,D('P28')*.7/4)+.35),800])
for k in range(12): ev['pop'].append([at('P30',.1+k*.12),300])
for p,f in [('P10',.7),('P22',.55),('P23',.35),('P30',.6)]: ev['ting'].append(at(p,D(p)*f))
k9=[i for i,x in enumerate(tl) if x['ch']==9][0];pv=tl[k9-1]
ev['tada']+=[at('P01',1.6),round(pv['t0']+pv['d']+.3,2),at('P30',D('P30')*.6)]
sa=min(5.5,max(2.4,D('P33')*.42))
ev['chime']+=[at('P33',.5),at('P33',sa+.1),at('P33',sa+1.2)]; ev['tada'].append(at('P33',D('P33')-1.5))
json.dump(ev,open('ev.json','w'))
print({k:len(v) for k,v in ev.items()}, d['total'])

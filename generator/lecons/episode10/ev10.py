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
P=[('P02',.1),('P02',.35),('P02',.5),('P02',.65),('P02',.8),('P03',.1),('P03',.55),('P03',.62),('P03',.69),('P03',.7),('P04',.6),('P05',.18),('P05',.355),('P05',.53),('P05',.705),
 ('P06',.45),('P07',.3),('P08',.25),('P08',.43),('P08',.61),('P09',.1),('P10',.1),('P10',.5),('P12',.55),('P13',.1),('P13',.25),('P13',.4),('P14',.55),('P15',.55),('P16',.2),
 ('P17',.25),('P18',.45),('P18',.55),('P18',.65),('P18',.75),('P19',.1),('P20',.1),('P20',.25),('P20',.4),('P20',.7),('P21',.1),('P21',.45),('P22',.1),('P22',.3),('P22',.7),
 ('P23',.1),('P24',.15),('P24',.25),('P25',.75),('P26',.1),('P26',.4),('P26',.7),('P27',.1),('P27',.2),('P27',.45),('P28',.12),('P29',.1),('P30',.1),('P31',.1),('P31',.5)]
for p,f in P: ev['pop'].append([at(p,D(p)*f),500])
for p in range(4): ev['pop'].append([at('P32',D('P32')*.12+p*min(1.6,D('P32')*.7/4)+.35),800])
for p,f in [('P12',.6),('P19',.75),('P26',.75),('P27',.5)]: ev['ting'].append(at(p,D(p)*f))
k9=[i for i,x in enumerate(tl) if x['ch']==9][0];pv=tl[k9-1]
ev['tada']+=[at('P01',1.6),round(pv['t0']+pv['d']+.3,2),at('P32',D('P32')*.85)]
sa=max(5.5,D('P33')*.42)
ev['chime']+=[at('P33',.5),at('P33',sa+.1),at('P33',sa+1.2)]; ev['tada'].append(at('P33',D('P33')-1.5))
json.dump(ev,open('ev.json','w'))
print({k:len(v) for k,v in ev.items()}, d['total'])

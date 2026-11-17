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
P=[('P02',.2),('P02',.1),('P03',.2),('P03',.45),('P04',.12),('P04',.42),('P04',.78),('P05',.35),('P06',.3),('P06',.55),('P06',.75),('P07',.45),('P08',.3),('P08',.6),
 ('P09',.1),('P09',.4),('P09',.72),('P10',.35),('P11',.35),('P11',.7),('P12',.45),('P12',.7),('P13',.5),('P14',.7),('P15',.25),('P15',.55),('P15',.75),('P16',.4),('P16',.7),('P16',.8),
 ('P17',.15),('P17',.55),('P19',.4),('P20',.6),('P21',.4),('P22',.4),('P23',.35),('P24',.3),('P24',.62),('P25',.45),('P27',.05),('P28',.05),('P29',.05),('P30',.05),
 ('P31',.4),('P32',.45),('P33',.6)]
for p,f in P: ev['pop'].append([at(p,D(p)*f),500])
for p in range(4): ev['pop'].append([at('P34',D('P34')*.15+p*min(1.6,D('P34')*.75/4)+.35),800])
for p,f in [('P15',.55),('P16',.7),('P23',.35),('P23',.5),('P12',.45)]: ev['ting'].append(at(p,D(p)*f))
k9=[i for i,x in enumerate(tl) if x['ch']==9][0];pv=tl[k9-1]
ev['tada']+=[at('P01',1.6),round(pv['t0']+pv['d']+.3,2),at('P34',D('P34')*.85)]
ev['chime'].append(at('P35',.5)); ev['tada'].append(at('P35',D('P35')-1.5))
json.dump(ev,open('ev.json','w'))
print({k:len(v) for k,v in ev.items()}, d['total'])

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
P=[('P02',.2),('P02',.35),('P02',.5),('P02',.7),('P03',.45),('P04',.35),('P04',.65),('P05',.45),('P05',.15),('P06',.4),('P06',.7),('P07',.15),('P07',.55),('P08',.12),('P08',.55),
 ('P09',.15),('P09',.5),('P09',.8),('P10',.3),('P11',.45),('P11',.72),('P12',.3),('P13',.5),('P14',.2),('P14',.45),('P15',.6),('P16',.3),('P16',.62),('P17',.5),('P18',.45),('P19',.45),
 ('P20',.35),('P20',.65),('P21',.35),('P21',.7),('P23',.12),('P23',.35),('P23',.7),('P24',.3),('P25',.25),('P26',.35),('P27',.4),('P28',.25),('P28',.55),('P29',.5),('P30',.5),
 ('P31',.55),('P31',.78),('P32',.5),('P33',.2),('P33',.45),('P33',.72)]
for p,f in P: ev['pop'].append([at(p,D(p)*f),500])
for p in range(4): ev['pop'].append([at('P34',D('P34')*.15+p*min(1.6,D('P34')*.75/4)+.35),800])
for p,f in [('P11',.72),('P17',.5),('P20',.65),('P33',.72),('P09',.8)]: ev['ting'].append(at(p,D(p)*f))
k9=[i for i,x in enumerate(tl) if x['ch']==9][0];pv=tl[k9-1]
ev['tada']+=[at('P01',1.6),round(pv['t0']+pv['d']+.3,2),at('P34',D('P34')*.85)]
ev['chime'].append(at('P35',.5)); ev['tada'].append(at('P35',D('P35')-1.5))
json.dump(ev,open('ev.json','w'))
print({k:len(v) for k,v in ev.items()}, d['total'])

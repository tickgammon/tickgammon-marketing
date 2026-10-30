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
for p,f in [('P08',.15),('P10',.0)]:
    for j in range(9): ev['click'].append(at(p,D(p)*f+.1+j*.12))
P=[('P02',.2),('P02',.4),('P02',.38),('P02',.62),('P03',.2),('P03',.3),('P03',.5),('P03',.55),('P04',.35),('P04',.5),('P04',.65),('P04',.8),('P06',.25),('P07',.6),('P08',.25),('P09',.25),('P09',.5),
 ('P11',.2),('P11',.4),('P11',.6),('P11',.8),('P12',.62),('P15',.3),('P16',.6),('P17',.2),('P18',.3),('P18',.4),('P18',.5),('P18',.6),('P19',.3),('P20',.2),('P21',.35),('P22',.2),('P22',.55),('P23',.15),('P23',.45),
 ('P24',.6),('P24',.68),('P24',.76),('P25',.55),('P26',.25),('P27',.25),('P28',.25),('P29',.4),('P29',.65),('P30',.62),('P31',.2),('P32',.2),('P33',.3),('P33',.55)]
for p,f in P: ev['pop'].append([at(p,D(p)*f if f<1 else f),500])
for p in range(4): ev['pop'].append([at('P34',D('P34')*.15+p*min(1.6,D('P34')*.75/4)+.35),800])
for p,f in [('P04',.9),('P15',.8),('P17',.8),('P19',.7),('P23',.5),('P30',.65)]: ev['ting'].append(at(p,D(p)*f))
k9=[i for i,x in enumerate(tl) if x['ch']==9][0];pv=tl[k9-1]
ev['tada']+=[at('P01',1.6),round(pv['t0']+pv['d']+.3,2),at('P34',D('P34')*.85)]
ev['chime'].append(at('P35',.5)); ev['tada'].append(at('P35',D('P35')-1.5))
json.dump(ev,open('ev.json','w'))
print({k:len(v) for k,v in ev.items()}, d['total'])

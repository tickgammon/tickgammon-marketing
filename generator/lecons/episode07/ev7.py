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
for p,f in [('P10',.05)]:
    for j in range(9): ev['click'].append(at(p,D(p)*f+.1+j*.12))
P=[('P02',.1),('P02',.2),('P02',.35),('P03',.3),('P03',.65),('P04',.7),('P05',.05),('P05',.3),('P05',.38),('P05',.65),('P06',.05),('P06',.3),('P06',.35),
 ('P07',.05),('P07',.15),('P07',.2),('P07',.45),('P08',.05),('P08',.25),('P09',.42),('P09',.68),('P10',.5),('P11',.05),('P11',.3),('P11',.6),('P12',.3),('P13',.05),('P13',.3),
 ('P14',.4),('P15',.05),('P15',.6),('P16',.35),('P16',.62),('P17',.4),('P18',.05),('P18',.45),('P19',.12),('P19',.55),('P20',.05),('P20',.4),('P21',.25),('P22',.6),
 ('P23',.25),('P23',.35),('P23',.45),('P23',.55),('P24',.2),('P24',.6),('P25',.05),('P25',.55),('P25',.7),('P27',.05),('P28',.05),('P29',.05),('P29',.4),('P30',.05),('P30',.4),('P30',.75),
 ('P31',.55),('P32',.2),('P32',.32),('P32',.44),('P32',.56),('P32',.68),('P33',.05),('P33',.5)]
for p,f in P: ev['pop'].append([at(p,D(p)*f if f<1 else f),500])
for p in range(4): ev['pop'].append([at('P34',D('P34')*.15+p*min(1.6,D('P34')*.75/4)+.35),800])
for p,f in [('P11',.6),('P16',.62),('P22',.6),('P25',.55),('P29',.4)]: ev['ting'].append(at(p,D(p)*f))
k9=[i for i,x in enumerate(tl) if x['ch']==9][0];pv=tl[k9-1]
ev['tada']+=[at('P01',1.6),round(pv['t0']+pv['d']+.3,2),at('P34',D('P34')*.85)]
ev['chime'].append(at('P35',.5)); ev['tada'].append(at('P35',D('P35')-1.5))
json.dump(ev,open('ev.json','w'))
print({k:len(v) for k,v in ev.items()}, d['total'])

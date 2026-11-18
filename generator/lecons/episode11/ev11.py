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
P=[('P02',.2,0),('P03',.2,0),('P03',.6,1),('P04',.2,0),('P04',.45,1),('P05',.2,0),('P05',.5,0),('P05',.7,0),('P05',.55,1),
 ('P06',.2,0),('P06',.25,1),('P06',.5,1),('P07',.4,1),('P08',.2,0),('P08',.3,1),('P08',.55,1),('P09',.15,0),('P10',.2,0),('P10',.25,1),('P10',.4,1),
 ('P11',.2,0),('P11',.2,1),('P11',.35,1),('P11',.65,1),('P12',.2,0),('P12',.3,1),('P12',.45,1),('P12',.6,1),('P13',.2,0),('P13',.25,1),('P13',.45,1),
 ('P14',.1,0),('P14',.2,1),('P14',.55,1),('P15',.15,0),('P15',.25,1),('P15',.55,1),('P16',.2,0),('P16',.45,1),('P17',.2,0),('P17',.3,1),
 ('P18',.15,0),('P18',.25,1),('P18',.5,1),('P18',.8,1),('P19',.2,0),('P19',.5,1),('P20',.1,0),('P20',.5,1),('P21',.15,0),('P21',.25,1),('P21',.5,1),
 ('P22',.15,0),('P22',.35,1),('P23',.2,0),('P23',.45,1),('P24',.2,0),('P24',.4,0),('P24',.75,1),('P25',.62,1),('P26',.2,0),('P26',.25,1),('P26',.45,1),
 ('P27',.2,0),('P27',.45,1),('P28',.15,0),('P28',.25,1),('P28',.45,1),('P29',.15,1),('P29',.37,1),('P29',.59,1),('P30',.35,1),('P30',.55,1),('P32',.55,1)]
for p,f,fr in P: ev['pop'].append([at(p,D(p)*f if fr else f),500])
for k in range(4): ev['pop'].append([at('P31',D('P31')*.12+k*min(1.6,D('P31')*.7/4)+.35),800])
for k in range(12): ev['pop'].append([at('P32',.15+k*.07),300])
for p,f in [('P04',.45),('P20',.45),('P22',.35),('P24',.75)]: ev['ting'].append(at(p,D(p)*f))
k9=[i for i,x in enumerate(tl) if x['ch']==9][0];pv=tl[k9-1]
ev['tada']+=[at('P01',1.6),round(pv['t0']+pv['d']+.3,2),at('P32',D('P32')*.85)]
sa=max(5.5,D('P33')*.42)
ev['chime']+=[at('P33',.5),at('P33',sa+.1),at('P33',sa+1.2)]; ev['tada'].append(at('P33',D('P33')-1.5))
json.dump(ev,open('ev.json','w'))
print({k:len(v) for k,v in ev.items()}, d['total'])

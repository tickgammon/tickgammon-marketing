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
ev['tada']+=[at('P01',1.6),at('P26',.8+2.4),at('P38',D('P38')*.55)]
for j in range(8): ev['click'].append(at('P13',.2+j*.12))
# cartes / chiffres qui apparaissent
for p,f in [('P02',.2),('P05',.4),('P07',.2),('P09',.3),('P10',.2),('P10',.55),('P18',.2),('P22',.2),('P22',.4),('P31',.2),('P31',.4),('P32',.2),('P32',.4),('P33',.3),('P33',.6),('P34',.2),('P34',.65),('P37',.15)]:
    ev['pop'].append([at(p,D(p)*f if f<1 else f),500])
for p in ('P08','P15','P17','P20','P25','P29','P30'): ev['ting'].append(at(p,D(p)*.6))
ev['chime'].append(at('P39',.5)); ev['tada'].append(at('P39',D('P39')-1.5))
json.dump(ev,open('ev.json','w'))
print({k:len(v) for k,v in ev.items()}, d['total'])

import json,sys
L=sys.argv[1]; SUF='' if L=='fr' else '_'+L
d=json.load(open(f'timeline{SUF}.json'));tl=d['tl'];T={x['p']:x for x in tl}
ev={"pop":[],"click":[],"ting":[],"whoosh":[],"tada":[],"chime":[]}
for a,b in zip(tl,tl[1:]):
    if a['ch']!=b['ch']: ev['whoosh'].append(round(a['t0']+a['d']+.15,2))
def at(p,x): return round(T[p]['t0']+x,2)
ev['tada'].append(at('P01',1.6))
for p,dur in (('P03',1.4),('P18',1.3)):
    k=0.3 if p=='P18' else 0
    for j in range(8): ev['click'].append(at(p,k+j*dur/8))
for p,i in (('P13',[.1,.35]),('P14',[0,.12,.24,.36,.48]),('P15',[0,.15,.3]),('P16',[0,.15,.3,.45,.6])):
    for x in i: ev['pop'].append([at(p,x+.3),700])
D16=T['P16']['d']
for k in range(4): ev['pop'].append([at('P16',D16*.32+k*.35+.3),500])
ev['pop'].append([at('P06',2.5),300])
ev['pop'].append([at('P26',T['P26']['d']*.3+.6),300]); ev['pop'].append([at('P34',T['P34']['d']*.3+.65),300])
for f in (.18,.45,.75): ev['ting'].append(at('P21',T['P21']['d']*f))
for f in (.05,.35,.62): ev['ting'].append(at('P24',T['P24']['d']*f))
for p in ('P36','P37','P38'): ev['ting'].append(at(p,.2))
ev['tada'].append(at('P38',T['P38']['d']*.7))
ev['chime'].append(at('P46',.5)); ev['tada'].append(at('P46',T['P46']['d']-1.5))
json.dump(ev,open(f'ev{SUF}.json','w'))
print(d['total'])

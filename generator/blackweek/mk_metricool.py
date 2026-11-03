# Posts Metricool des 2 vidéos Black Week — usage : python3 mk_metricool.py <commit> <fichier_sortie.json>
import json,sys
C=sys.argv[1]; OUTF=sys.argv[2]
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/%s/videos/blackweek/%%s_%%s_vertical.mp4'%C
AI={'fr':'🤖 Voix et animations créées avec l\'aide de l\'IA.','en':'🤖 Voice and animations created with the help of AI.','es':'🤖 Voz y animaciones creadas con ayuda de la IA.'}
H={'fr':'10:30','en':'14:00','es':'18:00'}
V={
'bw':('2026-11-23',
 {'fr':("🖤 C'est la Black Week sur TickGammon !\n-50 % sur la 1re année des packs annuels, -30 % sur le 1er mois des mensuels. Prix déjà barré, sans code. Jusqu'au 30/11.\n👉 https://www.tickgammon.com\n#backgammon","Black Week : les packs à -50 % 🖤 #shorts","Black Week -50 %"),
  'en':("🖤 It's Black Week on TickGammon!\n-50% on the 1st year of annual plans, -30% on the 1st month of monthly plans. Price already reduced, no code. Until 30/11.\n👉 https://www.tickgammon.com\n#backgammon","Black Week: plans at -50% 🖤 #shorts","Black Week -50%"),
  'es':("🖤 ¡Black Week en TickGammon!\n-50 % el 1.er año de los planes anuales, -30 % el 1.er mes de los mensuales. Sin código, hasta el 30/11.\n👉 https://www.tickgammon.com\n#backgammon","Black Week: planes a -50 % 🖤 #shorts","Black Week -50 %")}),
'bwfin':('2026-11-29',
 {'fr':("⏳ Black Week : dernières heures !\nJusqu'à demain 23:59 : -50 % sur la 1re année des packs annuels, -30 % sur le 1er mois des mensuels. Sans code.\n👉 https://www.tickgammon.com\n#backgammon","Black Week : dernières heures ⏳ #shorts","Black Week, dernières heures"),
  'en':("⏳ Black Week: final hours!\nUntil tomorrow 23:59: -50% on the 1st year of annual plans, -30% on the 1st month of monthly plans. No code needed.\n👉 https://www.tickgammon.com\n#backgammon","Black Week: final hours ⏳ #shorts","Black Week, final hours"),
  'es':("⏳ Black Week: ¡últimas horas!\nHasta mañana a las 23:59: -50 % el 1.er año de los planes anuales, -30 % el 1.er mes de los mensuales. Sin código.\n👉 https://www.tickgammon.com\n#backgammon","Black Week: últimas horas ⏳ #shorts","Black Week, últimas horas")}),
}
TAGS={'fr':['backgammon','tickgammon','black week'],'en':['backgammon','tickgammon','black week'],'es':['backgammon','tickgammon','black week']}
out=[]
for v,(d,TX) in V.items():
  for L in 'fr','en','es':
    txt,yt,t=TX[L]
    txt=txt+"\n"+AI[L]
    i={"autoPublish":True,"draft":False,"text":txt,"media":[R%(v,L)],
       "publicationDate":{"dateTime":d+"T"+H[L]+":00","timezone":"Europe/Paris"},
       "youtubeData":{"title":yt,"type":"short","privacy":"public","tags":TAGS[L],"category":"GAMING","madeForKids":False,"isAiGeneratedContent":True},
       "tiktokData":{"privacyOption":"PUBLIC_TO_EVERYONE","commercialContentOwnBrand":True,"title":t,"isAigc":True},
       "twitterData":{"tags":[]},"blueskyData":{"postLanguages":[L]},"firstCommentText":""}
    nets=["tiktok","youtube","bluesky","twitter"]
    if L=='fr':
      nets+=["facebook","linkedin"]; i["facebookData"]={"type":"REEL","title":t+" — TickGammon"}; i["linkedinData"]={"previewIncluded":True,"type":"post"}
    i["providers"]=[{"network":n} for n in nets]
    xl=len(txt)+sum(1 for ch in txt if ord(ch)>0x2000)+ (23-len('https://www.tickgammon.com'))
    assert xl<=280,(v,L,xl); assert len(txt)<=300,(v,L,len(txt)); assert len(yt)<=100
    out.append(i)
json.dump(out,open(OUTF,'w'),ensure_ascii=False,indent=1)
print(len(out))

# Posts Metricool de la vidéo pub Pack Sagesse — usage : python3 mk_metricool.py <commit> <fichier_sortie.json>
import json,sys
C=sys.argv[1]; OUTF=sys.argv[2]
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/%s/videos/packs/pack-sagesse-%%s.mp4'%C
AI={'fr':"🤖 Animations créées avec l'aide de l'IA.",'en':'🤖 Animations created with the help of AI.','es':'🤖 Animaciones creadas con ayuda de la IA.'}
H={'fr':'18:00','en':'19:00','es':'21:00'}
V={
'2026-11-17':{
 'fr':("🦉 Bloqué sur une position ? Avec le Pack Sagesse, l'IA trouve le meilleur coup, la chouette t'explique ton erreur et tu prends des cours avec un prof. Essai gratuit 7 jours.\n👉 https://www.tickgammon.com\n#backgammon","Progresse avec la chouette : Pack Sagesse 🦉 #shorts","Pack Sagesse"),
 'en':("🦉 Stuck on a position? With the Sagesse Pack, the AI finds the best move, the owl explains your mistake and you take lessons with a teacher. 7-day free trial.\n👉 https://www.tickgammon.com\n#backgammon","Level up with the owl: Sagesse Pack 🦉 #shorts","Sagesse Pack"),
 'es':("🦉 ¿Atascado en una posición? Con el Pack Sagesse, la IA encuentra la mejor jugada, la lechuza te explica tu error y tomas clases con un profesor. Prueba gratis 7 días.\n👉 https://www.tickgammon.com\n#backgammon","Progresa con la lechuza: Pack Sagesse 🦉 #shorts","Pack Sagesse")},
'2026-11-26':{
 'fr':("🖤 Black Week : le Pack Sagesse à -50 % la 1re année en annuel, -30 % le 1er mois en mensuel, jusqu'au 30/11. IA, explications de la chouette et cours avec un prof.\n👉 https://www.tickgammon.com\n#backgammon","Black Week : Pack Sagesse à -50 % 🖤 #shorts","Pack Sagesse -50 %"),
 'en':("🖤 Black Week: the Sagesse Pack at -50% on the 1st year (annual), -30% on the 1st month (monthly), until 30/11. AI, the owl's explanations and lessons with a teacher.\n👉 https://www.tickgammon.com\n#backgammon","Black Week: Sagesse Pack at -50% 🖤 #shorts","Sagesse Pack -50%"),
 'es':("🖤 Black Week: Pack Sagesse a -50 % el 1.er año (anual), -30 % el 1.er mes (mensual), hasta el 30/11. IA, explicaciones de la lechuza y clases.\n👉 https://www.tickgammon.com\n#backgammon","Black Week: Pack Sagesse a -50 % 🖤 #shorts","Pack Sagesse -50 %")},
}
TAGS=['backgammon','tickgammon','pack sagesse']
out=[]
for d,TX in V.items():
  for L in 'fr','en','es':
    txt,yt,t=TX[L]; txt=txt+"\n"+AI[L]
    i={"autoPublish":True,"draft":False,"text":txt,"media":[R%L],
       "publicationDate":{"dateTime":d+"T"+H[L]+":00","timezone":"Europe/Paris"},
       "youtubeData":{"title":yt,"type":"short","privacy":"public","tags":TAGS,"category":"GAMING","madeForKids":False,"isAiGeneratedContent":True},
       "tiktokData":{"privacyOption":"PUBLIC_TO_EVERYONE","commercialContentOwnBrand":True,"title":t,"isAigc":True},
       "twitterData":{"tags":[]},"blueskyData":{"postLanguages":[L]},"firstCommentText":""}
    nets=["tiktok","youtube","bluesky","twitter"]
    if L=='fr':
      nets+=["facebook","linkedin"]; i["facebookData"]={"type":"REEL","title":t+" — TickGammon"}; i["linkedinData"]={"previewIncluded":True,"type":"post"}
    i["providers"]=[{"network":n} for n in nets]
    xl=len(txt)+sum(1 for ch in txt if ord(ch)>0x2000)+(23-len('https://www.tickgammon.com'))
    assert xl<=280,(d,L,xl); assert len(txt)<=300,(d,L,len(txt)); assert len(yt)<=100
    out.append(i)
json.dump(out,open(OUTF,'w'),ensure_ascii=False,indent=1)
print(len(out))

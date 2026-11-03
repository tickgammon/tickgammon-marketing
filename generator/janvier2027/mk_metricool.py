# Posts Metricool de janvier 2027 — usage : python3 mk_metricool.py <commit>
import json,sys
C=sys.argv[1]
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/%s/videos/janvier2027/%%s_%%s_vertical.mp4'%C
IMG='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/%s/visuels/janvier2027/tournoi-hiver-2027-%%s.jpg'%C
AI={'fr':'🤖 Voix et animations créées avec l\'aide de l\'IA.','en':'🤖 Voice and animations created with the help of AI.','es':'🤖 Voz y animaciones creadas con ayuda de la IA.'}
AIimg={'fr':'🤖 Visuel créé avec l\'aide de l\'IA.','en':'🤖 Visual created with the help of AI.','es':'🤖 Imagen creada con ayuda de la IA.'}
H={'fr':'10:30','en':'14:00','es':'18:00'}
V={
'galette':('2027-01-04',
 {'fr':("🥮 La galette de la chouette est servie !\nDu 4 au 10 janvier, chaque partie contre un joueur = une part à choisir : TGC offerts, cosmétiques… et la fève 👑\n👉 https://www.tickgammon.com\n#backgammon","La galette de la chouette 🥮 Trouve la fève ! #shorts","La galette de la chouette"),
  'en':("🥮 The owl's king cake is served!\nJanuary 4 to 10, every game against a player = a slice to pick: TGC offered, cosmetics… and the lucky charm 👑\n👉 https://www.tickgammon.com\n#backgammon","The owl's king cake 🥮 Find the lucky charm! #shorts","The owl's king cake"),
  'es':("🥮 ¡El roscón de la lechuza está servido!\nDel 4 al 10 de enero, cada partida contra un jugador = una porción a elegir: TGC de regalo, cosméticos… y el haba 👑\n👉 https://www.tickgammon.com\n#backgammon","El roscón de la lechuza 🥮 ¡Encuentra el haba! #shorts","El roscón de la lechuza")}),
'soldes':('2027-01-13',
 {'fr':("❄️ Soldes d'hiver sur TickGammon !\nDu 13 au 26 janvier, -30 % sur les pions, plateaux, avatars et effets en TGC. Prix barré, sans code.\n👉 https://www.tickgammon.com\n#backgammon","Soldes d'hiver -30 % ❄️ #shorts","Soldes d'hiver"),
  'en':("❄️ Winter sale on TickGammon!\nJanuary 13 to 26, -30% on checkers, boards, avatars and effects in TGC. Reduced price, no code.\n👉 https://www.tickgammon.com\n#backgammon","Winter sale -30% ❄️ #shorts","Winter sale"),
  'es':("❄️ ¡Rebajas de invierno en TickGammon!\nDel 13 al 26 de enero, -30 % en fichas, tableros, avatares y efectos en TGC. Sin código.\n👉 https://www.tickgammon.com\n#backgammon","Rebajas de invierno -30 % ❄️ #shorts","Rebajas de invierno")}),
'tournoi':('2027-01-15',
 {'fr':("🏆 Tournoi Hiver 2027 : samedi 16 janvier à 21h !\nGratuit, 3 000 TGC offerts et le plateau exclusif Hiver 2027 au vainqueur.\n👉 https://www.tickgammon.com\n#backgammon","Tournoi Hiver 2027 🏆 samedi 21h #shorts","Tournoi Hiver 2027"),
  'en':("🏆 Winter 2027 tournament: Saturday January 16 at 9 PM (Paris)!\nFree, 3,000 TGC offered and the exclusive Winter 2027 board for the winner.\n👉 https://www.tickgammon.com\n#backgammon","Winter 2027 tournament 🏆 Saturday 9 PM #shorts","Winter 2027 tournament"),
  'es':("🏆 Torneo Invierno 2027: ¡sábado 16 de enero a las 21h (París)!\nGratis, 3.000 TGC de regalo y el tablero exclusivo Invierno 2027 al ganador.\n👉 https://www.tickgammon.com\n#backgammon","Torneo Invierno 2027 🏆 sábado 21h #shorts","Torneo Invierno 2027")}),
}
TAGS={'fr':['backgammon','tickgammon','jeu de société'],'en':['backgammon','tickgammon','board games'],'es':['backgammon','tickgammon','juegos de mesa']}
def xlen(t): return len(t)+sum(1 for ch in t if ord(ch)>0x2000)
out=[]
for v,(d,TX) in V.items():
  for L in 'fr','en','es':
    txt,yt,t=TX[L]; txt=txt+"\n"+AI[L]
    i={"autoPublish":True,"draft":False,"text":txt,"media":[R%(v,L)],
       "publicationDate":{"dateTime":d+"T"+H[L]+":00","timezone":"Europe/Paris"},
       "youtubeData":{"title":yt,"type":"short","privacy":"public","tags":TAGS[L],"category":"GAMING","madeForKids":False,"isAiGeneratedContent":True},
       "tiktokData":{"privacyOption":"PUBLIC_TO_EVERYONE","commercialContentOwnBrand":True,"title":t,"isAigc":True},
       "twitterData":{"tags":[]},"blueskyData":{"postLanguages":[L]},"firstCommentText":""}
    nets=["tiktok","youtube","bluesky","twitter"]
    if L=='fr':
      nets+=["facebook","linkedin"]; i["facebookData"]={"type":"REEL","title":t+" — TickGammon"}; i["linkedinData"]={"previewIncluded":True,"type":"post"}
    i["providers"]=[{"network":n} for n in nets]
    assert xlen(txt)<=278,(v,L,xlen(txt)); assert len(txt)<=300; assert len(yt)<=100
    out.append((d+"T"+H[L]+":00",json.dumps(i,ensure_ascii=False)))
# Rappel du tournoi le jour J (visuel carré)
RH={'fr':'18:30','en':'19:00','es':'19:30'}
RT={'fr':"⏰ Ce soir 21h : le tournoi Hiver 2027 !\nGratuit, 3 000 TGC offerts et le plateau exclusif Hiver 2027 au vainqueur. Inscris-toi dans Events.\n👉 https://www.tickgammon.com\n#backgammon",
    'en':"⏰ Tonight 9 PM (Paris): the Winter 2027 tournament!\nFree, 3,000 TGC offered and the exclusive Winter 2027 board for the winner. Sign up in Events.\n👉 https://www.tickgammon.com\n#backgammon",
    'es':"⏰ Esta noche 21h (París): ¡el torneo Invierno 2027!\nGratis, 3.000 TGC de regalo y el tablero exclusivo Invierno 2027 al ganador. Inscríbete en Events.\n👉 https://www.tickgammon.com\n#backgammon"}
for L in 'fr','en','es':
    txt=RT[L]+"\n"+AIimg[L]
    i={"autoPublish":True,"draft":False,"text":txt,"media":[IMG%L],
       "publicationDate":{"dateTime":"2027-01-16T"+RH[L]+":00","timezone":"Europe/Paris"},
       "twitterData":{"tags":[]},"blueskyData":{"postLanguages":[L]},"firstCommentText":""}
    nets=["twitter","bluesky"]
    if L=='fr': nets+=["facebook","linkedin"]; i["facebookData"]={"type":"POST"}; i["linkedinData"]={"previewIncluded":True,"type":"post"}
    i["providers"]=[{"network":n} for n in nets]
    assert xlen(txt)<=278,('rappel',L,xlen(txt)); assert len(txt)<=300
    out.append(("2027-01-16T"+RH[L]+":00",json.dumps(i,ensure_ascii=False)))
json.dump(out,open('/tmp/claude-0/-home-claude/df64ed30-987b-532f-99c1-0e43e84f8836/scratchpad/metricool_jan.json','w'),ensure_ascii=False)
print(len(out))

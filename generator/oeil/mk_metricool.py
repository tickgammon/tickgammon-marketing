# Posts Metricool « 👁️ L'œil de la chouette » (BROUILLONS à valider par Joyce) — usage : python3 mk_metricool.py <commit> <sortie.json>
import json,sys
C=sys.argv[1]; OUTF=sys.argv[2]
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/%s/videos/oeil-chouette/%%s_oeil_%%s_vertical.mp4'%C
AI={'fr':"🤖 Animations créées avec l'aide de l'IA.",'en':'🤖 Animations created with the help of AI.','es':'🤖 Animaciones creadas con ayuda de la IA.'}
U='https://www.tickgammon.com'
V=[
('tease1','2026-11-24',{'fr':'19:00','en':'19:30','es':'20:30'},
 {'fr':("🦉 Chut… La chouette ouvre l'œil.\nTon vrai plateau ne sera plus jamais le même. Rendez-vous mardi 1er décembre 👀\n"+U+"\n#backgammon","La chouette ouvre l'œil… 👀 #shorts","La chouette ouvre l'œil…"),
  'en':("🦉 Shh… The owl is opening its eye.\nYour real board will never be the same. See you Tuesday, December 1 👀\n"+U+"\n#backgammon","The owl opens its eye… 👀 #shorts","The owl opens its eye…"),
  'es':("🦉 Chis… La lechuza abre el ojo.\nTu tablero de verdad nunca volverá a ser igual. Nos vemos el martes 1 de diciembre 👀\n"+U+"\n#backgammon","La lechuza abre el ojo… 👀 #shorts","La lechuza abre el ojo…")}),
('tease2','2026-11-26',{'fr':'19:00','en':'19:30','es':'21:30'},
 {'fr':("📷 Indice : un plateau, une photo…\n… et la chouette sait déjà quoi jouer. Mardi 1er décembre 👀\n"+U+"\n#backgammon","Un plateau, une photo… 📷 #shorts","Un plateau, une photo…"),
  'en':("📷 Clue: one board, one photo…\n… and the owl already knows what to play. Tuesday, December 1 👀\n"+U+"\n#backgammon","One board, one photo… 📷 #shorts","One board, one photo…"),
  'es':("📷 Pista: un tablero, una foto…\n… y la lechuza ya sabe qué jugar. Martes 1 de diciembre 👀\n"+U+"\n#backgammon","Un tablero, una foto… 📷 #shorts","Un tablero, una foto…")}),
('launch','2026-12-01',{'fr':'10:30','en':'14:00','es':'18:00'},
 {'fr':("👁️ Nouveau : L'œil de la chouette !\nPrends ton vrai plateau en photo : la chouette lit la position et te donne le meilleur coup, expliqué. 3 photos offertes à tous jusqu'au 8/12 📷\n"+U+"\n#backgammon","L'œil de la chouette : ton vrai plateau en photo 📷 #shorts","L'œil de la chouette"),
  'en':("👁️ New: The owl's eye!\nTake a photo of your real board: the owl reads the position and gives you the best move, explained. 3 free photos for everyone until Dec 8 📷\n"+U+"\n#backgammon","The owl's eye: your real board in one photo 📷 #shorts","The owl's eye"),
  'es':("👁️ Nuevo: ¡El ojo de la lechuza!\nHaz una foto de tu tablero real: la lechuza lee la posición y te da la mejor jugada, explicada. 3 fotos gratis hasta el 8/12 📷\n"+U+"\n#backgammon","El ojo de la lechuza: tu tablero en una foto 📷 #shorts","El ojo de la lechuza")}),
]
LINKEDIN_FR=("👁️ Nouveau sur TickGammon : L'œil de la chouette.\n\nAu club ou au café, une position vous intrigue après la partie ? Prenez le plateau en photo : la chouette lit la position (pions et dés), l'analyse gnubg donne les meilleurs coups, et la chouette explique pourquoi.\n\n🎁 3 photos offertes à tous du 1er au 8 décembre, et -30 % sur le 1er mois du Pack Sagesse mensuel.\n\n"+U+"\n#backgammon")
TAGS=['backgammon','tickgammon','analyse']
out=[]
for v,d,H,TX in V:
  for L in 'fr','en','es':
    txt,yt,t=TX[L]; txt=txt+"\n"+AI[L]
    i={"autoPublish":True,"draft":True,"text":txt,"media":[R%(v,L)],
       "publicationDate":{"dateTime":d+"T"+H[L]+":00","timezone":"Europe/Paris"},
       "youtubeData":{"title":yt,"type":"short","privacy":"public","tags":TAGS,"category":"GAMING","madeForKids":False,"isAiGeneratedContent":True},
       "tiktokData":{"privacyOption":"PUBLIC_TO_EVERYONE","commercialContentOwnBrand":True,"title":t,"isAigc":True},
       "twitterData":{"tags":[]},"blueskyData":{"postLanguages":[L]},"firstCommentText":""}
    nets=["tiktok","youtube","bluesky","twitter"]
    if L=='fr':
      nets+=["facebook"]; i["facebookData"]={"type":"REEL","title":t+" — TickGammon"}
    i["providers"]=[{"network":n} for n in nets]
    xl=len(txt)+sum(1 for ch in txt if ord(ch)>0x2000)+(23-len(U))
    assert xl<=280,(v,L,xl); assert len(txt)<=300,(v,L,len(txt)); assert len(yt)<=100
    out.append(i)
  # LinkedIn FR du lancement : post à part (texte plus long, même vidéo)
  if v=='launch':
    out.append({"autoPublish":True,"draft":True,"text":LINKEDIN_FR+"\n"+AI['fr'],"media":[R%(v,'fr')],
      "publicationDate":{"dateTime":d+"T10:30:00","timezone":"Europe/Paris"},
      "providers":[{"network":"linkedin"}],"linkedinData":{"previewIncluded":True,"type":"post"},"firstCommentText":""})
json.dump(out,open(OUTF,'w'),ensure_ascii=False,indent=1)
print(len(out))

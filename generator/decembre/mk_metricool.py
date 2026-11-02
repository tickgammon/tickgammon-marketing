# Posts Metricool des 4 vidéos de décembre — usage : python3 mk_metricool.py <commit>
import json,sys
C=sys.argv[1]
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/%s/videos/decembre/%%s_%%s_vertical.mp4'%C
AI={'fr':'🤖 Voix et animations créées avec l\'aide de l\'IA.','en':'🤖 Voice and animations created with the help of AI.','es':'🤖 Voz y animaciones creadas con ayuda de la IA.'}
V={
'avent':('2026-11-30',{'fr':'10:30','en':'14:00','es':'18:00'},
 {'fr':("🎁 Chut… demain, la chouette ouvre la 1re case de son calendrier de l'Avent !\nDu 1er au 24 décembre, une case chaque jour sur l'accueil : des TGC offerts et des objets d'hiver 🤫\n👉 https://www.tickgammon.com\n#backgammon #calendrierdelavent","Demain, la 1re case du calendrier de l'Avent 🎁 #shorts","Calendrier de l'Avent"),
  'en':("🎁 Shh… tomorrow, the owl opens the 1st door of its Advent calendar!\nDecember 1 to 24, one door every day on the home screen: free TGC and winter items 🤫\n👉 https://www.tickgammon.com\n#backgammon #adventcalendar","Tomorrow, the 1st door of the Advent calendar 🎁 #shorts","Advent calendar"),
  'es':("🎁 Chis… mañana, la lechuza abre la 1.ª casilla de su calendario de Adviento.\nDel 1 al 24 de diciembre, una casilla cada día en la pantalla de inicio: TGC de regalo y objetos de invierno 🤫\n👉 https://www.tickgammon.com\n#backgammon #adviento","Mañana, la 1.ª casilla del calendario de Adviento 🎁 #shorts","Calendario de Adviento")}),
'plateau':('2026-12-14',{'fr':'10:30','en':'14:00','es':'18:00'},
 {'fr':("🎄 Le Plateau de Noël est arrivé ! Nuit de Noël, sapins dorés et la chouette de Noël au centre, 2 500 TGC.\nEt les pions Hiver ❄️ et Sapin ⭐ à 500 TGC.\n👉 https://www.tickgammon.com\n#backgammon #noel","Le Plateau de Noël est arrivé 🎄 #shorts","Le Plateau de Noël"),
  'en':("🎄 The Christmas board is here! Christmas night, golden trees and the Christmas owl in the middle, 2,500 TGC.\nPlus Winter ❄️ and Fir tree ⭐ checkers at 500 TGC.\n👉 https://www.tickgammon.com\n#backgammon #christmas","The Christmas board is here 🎄 #shorts","The Christmas board"),
  'es':("🎄 ¡Llegó el tablero de Navidad! Noche de Navidad, abetos dorados y la lechuza navideña en el centro, 2.500 TGC.\nY las fichas Invierno ❄️ y Abeto ⭐ a 500 TGC.\n👉 https://www.tickgammon.com\n#backgammon #navidad","Llegó el tablero de Navidad 🎄 #shorts","El tablero de Navidad")}),
'noel':('2026-12-25',{'fr':'10:30','en':'14:00','es':'18:00'},
 {'fr':("🎅 Joyeux Noël de toute l'équipe TickGammon !\nAujourd'hui encore, le bouton 🎁 Bonus te donne le double de TGC.\n👉 https://www.tickgammon.com\n#backgammon #joyeuxnoel","Joyeux Noël 🎅 Bonus TGC ×2 #shorts","Joyeux Noël"),
  'en':("🎅 Merry Christmas from the whole TickGammon team!\nToday too, the 🎁 Bonus button gives you double TGC.\n👉 https://www.tickgammon.com\n#backgammon #merrychristmas","Merry Christmas 🎅 TGC bonus ×2 #shorts","Merry Christmas"),
  'es':("🎅 ¡Feliz Navidad de todo el equipo de TickGammon!\nHoy también, el botón 🎁 Bonus te da el doble de TGC.\n👉 https://www.tickgammon.com\n#backgammon #feliznavidad","Feliz Navidad 🎅 Bonus de TGC ×2 #shorts","Feliz Navidad")}),
'voeux':('2026-12-31',{'fr':'18:00','en':'19:00','es':'20:00'},
 {'fr':("🥂 Merci pour cette première année sur TickGammon !\nLa chouette vous souhaite une très belle année 2027. On se retrouve autour du plateau 🎲\n👉 https://www.tickgammon.com\n#backgammon #bonneannee","Bonne année 2027 🥂 Merci pour cette 1re année #shorts","Bonne année 2027"),
  'en':("🥂 Thank you for this first year on TickGammon!\nThe owl wishes you a wonderful 2027. See you around the board 🎲\n👉 https://www.tickgammon.com\n#backgammon #happynewyear","Happy New Year 2027 🥂 Thanks for this first year #shorts","Happy New Year 2027"),
  'es':("🥂 ¡Gracias por este primer año en TickGammon!\nLa lechuza os desea un feliz 2027. Nos vemos alrededor del tablero 🎲\n👉 https://www.tickgammon.com\n#backgammon #felizañonuevo","Feliz Año 2027 🥂 Gracias por este primer año #shorts","Feliz Año 2027")}),
}
TAGS={'fr':['backgammon','tickgammon','jeu de société'],'en':['backgammon','tickgammon','board games'],'es':['backgammon','tickgammon','juegos de mesa']}
out=[]
for v,(d,H,TX) in V.items():
  for L in 'fr','en','es':
    txt,yt,t=TX[L]
    i={"autoPublish":True,"draft":False,"text":txt,"media":[R%(v,L)],
       "publicationDate":{"dateTime":d+"T"+H[L]+":00","timezone":"Europe/Paris"},
       "youtubeData":{"title":yt,"type":"short","privacy":"public","tags":TAGS[L],"category":"GAMING","madeForKids":False,"isAiGeneratedContent":True},
       "tiktokData":{"privacyOption":"PUBLIC_TO_EVERYONE","commercialContentOwnBrand":True,"title":t,"isAigc":True},
       "twitterData":{"tags":[]},"blueskyData":{"postLanguages":[L]},"firstCommentText":""}
    nets=["tiktok","youtube","bluesky","twitter"]
    if L=='fr':
      nets+=["facebook","linkedin"]; i["facebookData"]={"type":"REEL","title":t+" — TickGammon"}; i["linkedinData"]={"previewIncluded":True,"type":"post"}
    i["providers"]=[{"network":n} for n in nets]
    txt=txt+"\n"+AI[L]
    i["text"]=txt
    assert len(txt)<=300,(v,L,len(txt)); assert len(yt)<=100
    i["text"]=txt  # Bluesky ≤ 300
    out.append((d+"T"+H[L]+":00+01:00",json.dumps(i,ensure_ascii=False)))
json.dump(out,open('/tmp/claude-0/-home-claude/df64ed30-987b-532f-99c1-0e43e84f8836/scratchpad/metricool_dec.json','w'),ensure_ascii=False)
print(len(out))

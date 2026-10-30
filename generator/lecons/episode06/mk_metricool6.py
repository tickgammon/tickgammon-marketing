import json
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/main/videos/lecons/episode06/shorts/lecon6_%s_chap%d_9x16.mp4'
D=['2027-01-04','2027-01-05','2027-01-06','2027-01-08','2027-01-09','2027-01-11','2027-01-12','2027-01-14']
T={'fr':['Le principe','Les trois rôles','Le tirage','Les places tournent','Les points','Un videau chacun','Pourquoi on aime','Conseils'],
'en':['The idea','The three roles','The draw','Rotating places','The points','A cube each','Why we love it','Tips'],
'es':['La idea','Los tres papeles','El sorteo','Los puestos giran','Los puntos','Un cubo para cada uno','Por qué gusta','Consejos']}
H={'fr':["Le backgammon à 3, 4, 5 joueurs ou plus ? C'est la chouette !","Le box, le capitaine et l'équipe : qui fait quoi ?","Qui prend le box ? On tire au sort !","Le box gagne ? Il reste. Le capitaine gagne ? Il prend sa place.","Le box gagne : 3 points d'un coup. Il perd un gammon : 6 points !","Un videau pour chaque joueur de l'équipe : ça change tout.","On apprend vite, c'est convivial et c'est stratégique.","Dans le box, soyez prudent : une erreur coûte plusieurs fois !"],
'en':["Backgammon with 3, 4, 5 or more players? That's the chouette!","The box, the captain and the team: who does what?","Who takes the box? Draw lots!","The box wins? They stay. The captain wins? They take the box.","The box wins: 3 points at once. Loses a gammon: 6 points!","A cube for every team player: that changes everything.","You learn fast, it's social and it's strategic.","In the box, be careful: a mistake costs you several times over!"],
'es':["¿Backgammon entre 3, 4, 5 jugadores o más? ¡Es la chouette!","El box, el capitán y el equipo: ¿quién hace qué?","¿Quién ocupa el box? ¡Se sortea!","¿Gana el box? Se queda. ¿Gana el capitán? Ocupa el box.","El box gana: 3 puntos de golpe. Pierde un gammon: ¡6 puntos!","Un cubo para cada jugador del equipo: eso lo cambia todo.","Se aprende rápido, es muy social y es estratégica.","En el box, sed prudentes: ¡un error cuesta varias veces!"]}
S={'fr':("🦉 Les leçons de la chouette · Leçon 6, chapitre %d : %s\n%s\nLeçon complète sur YouTube · jouez gratuitement 👉 https://www.tickgammon.com\n#backgammon #jeudesociete","%s 🦉 La chouette au backgammon #shorts",["backgammon","chouette backgammon","jeu de société","tickgammon"],"12:30:00"),
'en':("🦉 The Owl's Lessons · Lesson 6, chapter %d: %s\n%s\nFull lesson on YouTube · play for free 👉 https://www.tickgammon.com\n#backgammon #boardgames","%s 🦉 The backgammon chouette #shorts",["backgammon","backgammon chouette","board games","tickgammon"],"16:00:00"),
'es':("🦉 Las lecciones de la lechuza · Lección 6, capítulo %d: %s\n%s\nLección completa en YouTube · juega gratis 👉 https://www.tickgammon.com\n#backgammon #juegosdemesa","%s 🦉 La chouette en backgammon #shorts",["backgammon","chouette backgammon","juegos de mesa","tickgammon"],"20:00:00")}
out=[]
for c in range(8):
  for L in 'fr','en','es':
    txt,yt,tags,h=S[L]; t=T[L][c]
    i={"autoPublish":True,"draft":False,"text":txt%(c+1,t,H[L][c]),"media":[R%(L,c+1)],
       "publicationDate":{"dateTime":D[c]+"T"+h,"timezone":"Europe/Paris"},
       "youtubeData":{"title":yt%t,"type":"short","privacy":"public","tags":tags,"category":"EDUCATION","madeForKids":False,"isAiGeneratedContent":True},
       "tiktokData":{"privacyOption":"PUBLIC_TO_EVERYONE","commercialContentOwnBrand":True,"title":t,"isAigc":True}}
    if L=='fr':
      i["providers"]=[{"network":n} for n in ["twitter","facebook","tiktok","youtube","bluesky"]]
      i["twitterData"]={"tags":[]};i["facebookData"]={"type":"REEL","title":t+" — Les leçons de la chouette"};i["blueskyData"]={"postLanguages":["fr"]}
      i["mediaAltText"]=["Vidéo : la chouette de TickGammon explique « %s » (la chouette au backgammon)"%t]
      assert len(i["text"])<=300,len(i["text"])
    else: i["providers"]=[{"network":"tiktok"},{"network":"youtube"}]
    assert len(i["youtubeData"]["title"])<=100
    out.append((D[c]+"T"+h+"+01:00",json.dumps(i,ensure_ascii=False)))
json.dump(out,open('metricool6.json','w'),ensure_ascii=False)
print(len(out))

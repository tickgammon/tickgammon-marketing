import json
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/main/videos/lecons/episode07/shorts/lecon7_%s_chap%d_9x16.mp4'
D=['2027-01-18','2027-01-19','2027-01-20','2027-01-22','2027-01-23','2027-01-25','2027-01-26','2027-01-28']
T={'fr':["Pourquoi l'ordinateur",'GNU Backgammon','Les dés sont honnêtes',"L'analyse",'Résultat ≠ jeu',"L'Entraînement",'La méthode','Pour débuter'],
'en':['Why the computer','GNU Backgammon','Honest dice','The analysis','Result ≠ play','Training','The method','Getting started'],
'es':['Por qué el ordenador','GNU Backgammon','Dados honestos','El análisis','Resultado ≠ juego','Entrenamiento','El método','Para empezar']}
H={'fr':["Un adversaire dispo 24 h/24, sans pression et très exigeant.","Le robot de TickGammon s'appuie sur l'un des meilleurs programmes au monde.","L'ordinateur triche-t-il avec les dés ? Non, et voici son vrai secret.","L'analyse vous montre le meilleur coup… et combien votre erreur a coûté.","Une victoire peut cacher de grosses erreurs. L'analyse dit la vérité !","Rejouez des positions et comprenez enfin vos erreurs.","3 étapes pour progresser : jouer, analyser, rejouer.","Vous débutez ? Perdre au début, c'est normal. Voici comment progresser."],
'en':["An opponent available 24/7, with no pressure and very demanding.","The TickGammon bot is built on one of the best programs in the world.","Does the computer cheat with the dice? No, and here's its real secret.","The analysis shows you the best move… and how much your mistake cost.","A win can hide big mistakes. The analysis tells the truth!","Replay positions and finally understand your mistakes.","3 steps to improve: play, analyse, replay.","Just starting out? Losing at first is normal. Here's how to improve."],
'es':["Un adversario disponible 24 h, sin presión y muy exigente.","El robot de TickGammon se basa en uno de los mejores programas del mundo.","¿Hace trampa el ordenador con los dados? No, y este es su verdadero secreto.","El análisis os muestra la mejor jugada… y cuánto os costó el error.","Una victoria puede esconder errores grandes. ¡El análisis dice la verdad!","Volved a jugar posiciones y entended por fin vuestros errores.","3 pasos para progresar: jugar, analizar, volver a jugar.","¿Estáis empezando? Perder al principio es normal. Así se progresa."]}
S={'fr':("🦉 Les leçons de la chouette · Leçon 7, chapitre %d : %s\n%s\nLeçon complète sur YouTube · jouez gratuitement 👉 https://www.tickgammon.com\n#backgammon #jeudesociete","%s 🦉 Progresser contre l'ordinateur #shorts",["backgammon","backgammon contre l'ordinateur","GNU Backgammon","tickgammon"],"12:30:00"),
'en':("🦉 The Owl's Lessons · Lesson 7, chapter %d: %s\n%s\nFull lesson on YouTube · play for free 👉 https://www.tickgammon.com\n#backgammon #boardgames","%s 🦉 Improving against the computer #shorts",["backgammon","backgammon against the computer","GNU Backgammon","tickgammon"],"16:00:00"),
'es':("🦉 Las lecciones de la lechuza · Lección 7, capítulo %d: %s\n%s\nLección completa en YouTube · juega gratis 👉 https://www.tickgammon.com\n#backgammon #juegosdemesa","%s 🦉 Progresar contra el ordenador #shorts",["backgammon","backgammon contra el ordenador","GNU Backgammon","tickgammon"],"20:00:00")}
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
      i["mediaAltText"]=["Vidéo : la chouette de TickGammon explique « %s » (progresser contre l'ordinateur)"%t]
      assert len(i["text"])<=300,len(i["text"])
    else: i["providers"]=[{"network":"tiktok"},{"network":"youtube"}]
    assert len(i["youtubeData"]["title"])<=100
    out.append((D[c]+"T"+h+"+01:00",json.dumps(i,ensure_ascii=False)))
json.dump(out,open('metricool7.json','w'),ensure_ascii=False)
print(len(out))

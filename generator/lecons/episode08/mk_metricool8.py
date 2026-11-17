import json
import sys
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/'+sys.argv[1]+'/videos/lecons/episode08/shorts/lecon8_%s_chap%d_9x16.mp4'
D=['2027-02-01','2027-02-02','2027-02-03','2027-02-05','2027-02-06','2027-02-08','2027-02-09','2027-02-11']
T={'fr':['Jouer en ligne','Formats et rythmes',"L'ELO","Comment l'ELO bouge","L'expérience",'Le classement','Quatre conseils','Le videau en ligne'],
'en':['Playing online','Formats and speeds','ELO','How ELO moves','Experience','The ranking','Four tips','The cube online'],
'es':['Jugar en línea','Formatos y ritmos','El ELO','Cómo se mueve el ELO','La experiencia','La clasificación','Cuatro consejos','El cubo en línea']}
H={'fr':["Navigateur, Android ou Windows : un seul compte, et c'est gratuit.","Zen, Classique, Blitz ou Bullet : à vous de choisir le rythme !","Tout le monde commence à 1500. Voici comment marche l'ELO.","Battre plus fort que soi rapporte gros… perdre contre plus faible coûte cher !","Pourquoi votre ELO bouge beaucoup pendant vos 50 premières parties.","Classement, paliers ELO et succès : la vitrine de vos progrès.","4 conseils simples pour faire grimper votre ELO.","En match, le videau change tout. Pensez à la règle des 25 % !"],
'en':["Browser, Android or Windows: one account, and it's free.","Zen, Classic, Blitz or Bullet: you choose the pace!","Everyone starts at 1500. Here's how the ELO rating works.","Beating a stronger player pays off… losing to a weaker one costs a lot!","Why your rating moves a lot during your first 50 games.","Rankings, rating milestones and achievements: the showcase of your progress.","4 simple tips to make your rating climb.","In a match, the cube changes everything. Remember the 25% rule!"],
'es':["Navegador, Android o Windows: una sola cuenta, y es gratis.","Zen, Clásico, Blitz o Bullet: ¡elegid vuestro ritmo!","Todo el mundo empieza con 1500. Así funciona el ELO.","Ganar a alguien más fuerte da mucho… ¡perder contra alguien más débil sale caro!","Por qué vuestro ELO se mueve mucho en vuestras 50 primeras partidas.","Clasificación, niveles de ELO y logros: el escaparate de vuestro progreso.","4 consejos sencillos para hacer subir vuestro ELO.","En un match, el cubo lo cambia todo. ¡Pensad en la regla del 25 %!"]}
S={'fr':("🦉 Les leçons de la chouette · Leçon 8, chapitre %d : %s\n%s\nLeçon complète sur YouTube · jouez gratuitement 👉 https://www.tickgammon.com\n#backgammon #jeudesociete","%s 🦉 Jouer en ligne et l'ELO #shorts",["backgammon","backgammon en ligne","ELO","tickgammon"],"12:30:00"),
'en':("🦉 The Owl's Lessons · Lesson 8, chapter %d: %s\n%s\nFull lesson on YouTube · play for free 👉 https://www.tickgammon.com\n#backgammon #boardgames","%s 🦉 Playing online and ELO #shorts",["backgammon","online backgammon","ELO","tickgammon"],"16:00:00"),
'es':("🦉 Las lecciones de la lechuza · Lección 8, capítulo %d: %s\n%s\nLección completa en YouTube · juega gratis 👉 https://www.tickgammon.com\n#backgammon #juegosdemesa","%s 🦉 Jugar en línea y el ELO #shorts",["backgammon","backgammon en línea","ELO","tickgammon"],"20:00:00")}
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
      i["mediaAltText"]=["Vidéo : la chouette de TickGammon explique « %s » (jouer en ligne et l'ELO)"%t]
      assert len(i["text"])<=280,len(i["text"])
    else: i["providers"]=[{"network":"tiktok"},{"network":"youtube"}]
    assert len(i["youtubeData"]["title"])<=100
    out.append((D[c]+"T"+h+"+01:00",json.dumps(i,ensure_ascii=False)))
json.dump(out,open('metricool8.json','w'),ensure_ascii=False)
print(len(out))

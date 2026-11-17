import json
import sys
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/'+sys.argv[1]+'/videos/lecons/episode10/shorts/lecon10_%s_chap%d_9x16.mp4'
# Leçon 10 : Shorts du 1er au 13/03/2027 (pas les vendredis de Friday Cup, ni le dimanche, ni le mercredi de l'annonce)
D=['2027-03-01','2027-03-02','2027-03-04','2027-03-06','2027-03-08','2027-03-09','2027-03-11','2027-03-13']
T={'fr':['Une seule famille','Le même matériel','Le backgammon','Le jacquet : le départ','Le jacquet : bloquer','Le trictrac','Le mot « trictrac »','En résumé'],
'en':['One family','The same equipment','Backgammon','Jacquet: the start','Jacquet: blocking','Trictrac','The word "trictrac"','In short'],
'es':['Una sola familia','El mismo material','El backgammon','El jacquet: la salida','El jacquet: bloquear','El trictrac','La palabra «trictrac»','En resumen']}
H={'fr':["Backgammon, jacquet, trictrac : une seule famille, les jeux de tables.","15 pions, 2 dés, 24 flèches : le matériel ne change presque pas.","Sens opposés, frappe et videau : c'est le backgammon.","Au jacquet : 15 pions sur une seule flèche, et tout le monde tourne dans le même sens !","Au jacquet, on ne frappe jamais : un seul pion suffit à bloquer.","Au trictrac, on gagne en marquant des points, avec jetons et fiches.","Pourquoi votre grand-père dit « trictrac » pour le backgammon.","Backgammon, jacquet, trictrac : le tableau pour tout comparer."],
'en':["Backgammon, jacquet, trictrac: one family, the tables games.","15 checkers, 2 dice, 24 points: the equipment hardly changes.","Opposite directions, hitting and the cube: that's backgammon.","In jacquet: 15 checkers on a single point, and everyone goes round the same way!","In jacquet, you never hit: a single checker is enough to block.","In trictrac, you win by scoring points, with tokens and pegs.","Why a French grandfather says \"trictrac\" for backgammon.","Backgammon, jacquet, trictrac: the table to compare everything."],
'es':["Backgammon, jacquet, trictrac: una sola familia, los juegos de tablas.","15 fichas, 2 dados, 24 puntas: el material casi no cambia.","Sentidos opuestos, golpes y cubo: eso es el backgammon.","En el jacquet: 15 fichas en una sola punta, ¡y todos giran en el mismo sentido!","En el jacquet nunca se golpea: una sola ficha basta para bloquear.","En el trictrac se gana marcando puntos, con fichas y clavijas.","Por qué un abuelo francés dice «trictrac» al backgammon.","Backgammon, jacquet, trictrac: la tabla para compararlo todo."]}
S={'fr':("🦉 Les leçons de la chouette · Leçon 10, chapitre %d : %s\n%s\nLeçon complète sur YouTube · jouez gratuitement 👉 https://www.tickgammon.com\n#backgammon #jeudesociete","%s 🦉 Jacquet, trictrac et backgammon #shorts",["backgammon","jacquet","trictrac","tickgammon"],"12:30:00"),
'en':("🦉 The Owl's Lessons · Lesson 10, chapter %d: %s\n%s\nFull lesson on YouTube · play for free 👉 https://www.tickgammon.com\n#backgammon #boardgames","%s 🦉 Jacquet, trictrac and backgammon #shorts",["backgammon","jacquet","trictrac","tickgammon"],"16:00:00"),
'es':("🦉 Las lecciones de la lechuza · Lección 10, capítulo %d: %s\n%s\nLección completa en YouTube · juega gratis 👉 https://www.tickgammon.com\n#backgammon #juegosdemesa","%s 🦉 Jacquet, trictrac y backgammon #shorts",["backgammon","jacquet","trictrac","tickgammon"],"20:00:00")}
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
      i["mediaAltText"]=["Vidéo : la chouette de TickGammon explique « %s » (jacquet, trictrac et backgammon)"%t]
      assert len(i["text"])<=280,len(i["text"])
    else: i["providers"]=[{"network":"tiktok"},{"network":"youtube"}]
    assert len(i["youtubeData"]["title"])<=100
    out.append((D[c]+"T"+h+"+01:00",json.dumps(i,ensure_ascii=False)))
json.dump(out,open('metricool10.json','w'),ensure_ascii=False)
print(len(out))

assert all('IA' not in json.loads(x)['text'] and ' AI' not in json.loads(x)['text'] for _,x in out)

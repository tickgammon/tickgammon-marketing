import json
import sys
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/'+sys.argv[1]+'/videos/lecons/episode11/shorts/lecon11_%s_chap%d_9x16.mp4'
# Leçon 11 : Shorts du 15 au 27/03/2027 (pas les vendredis de Friday Cup, ni le dimanche, ni le mercredi de l'annonce)
D=['2027-03-15','2027-03-16','2027-03-18','2027-03-20','2027-03-22','2027-03-23','2027-03-25','2027-03-27']
T={'fr':['Les lointains ancêtres','Rome : la tabula','La Perse et le nard','Le Moyen Âge','Le nom « backgammon »',"Le videau et l'âge d'or",'Les ordinateurs',"Aujourd'hui : en ligne"],
'en':['Distant ancestors','Rome: tabula','Persia and nard','The Middle Ages','The name "backgammon"','The cube and the golden age','Computers','Today: online'],
'es':['Los lejanos antepasados','Roma: la tabula','Persia y el nard','La Edad Media','El nombre «backgammon»','El cubo y la edad de oro','Los ordenadores','Hoy: en línea']}
H={'fr':["Il y a 4 500 ans, on jouait déjà au jeu royal d'Ur.","24 cases, 15 pions, et un empereur qui perd… avec trois dés !","La légende du sage Bozorgmehr et la naissance du nard.","Dans les châteaux comme dans les tavernes : tout le monde joue !","D'où vient le mot « backgammon » ? Réponse en 1 minute.","1920, New York : une petite invention change tout, le videau.","Quand un ordinateur apprend seul… et corrige les champions.","Un jeu vieux de 4 500 ans, désormais en ligne."],
'en':["4,500 years ago, people were already playing the Royal Game of Ur.","24 points, 15 checkers, and an emperor who loses… with three dice!","The legend of the sage Bozorgmehr and the birth of nard.","In castles and in taverns alike: everyone plays!","Where does the word \"backgammon\" come from? The answer in 1 minute.","1920s New York: a small invention changes everything, the doubling cube.","When a computer learns on its own… and corrects the champions.","A 4,500-year-old game, now online."],
'es':["Hace 4500 años ya se jugaba al juego real de Ur.","24 casillas, 15 fichas y un emperador que pierde… ¡con tres dados!","La leyenda del sabio Bozorgmehr y el nacimiento del nard.","En los castillos y en las tabernas: ¡todo el mundo juega!","¿De dónde viene la palabra «backgammon»? La respuesta en 1 minuto.","Nueva York, años 20: un pequeño invento lo cambia todo, el cubo doblador.","Cuando un ordenador aprende solo… y corrige a los campeones.","Un juego de 4500 años, ahora en línea."]}
S={'fr':("🦉 Les leçons de la chouette · Leçon 11, chapitre %d : %s\n%s\nLeçon complète sur YouTube · jouez gratuitement 👉 https://www.tickgammon.com\n#backgammon #jeudesociete","%s 🦉 L'histoire du backgammon #shorts",["backgammon","histoire du backgammon","jeu de société","tickgammon"],"12:30:00"),
'en':("🦉 The Owl's Lessons · Lesson 11, chapter %d: %s\n%s\nFull lesson on YouTube · play for free 👉 https://www.tickgammon.com\n#backgammon #boardgames","%s 🦉 The history of backgammon #shorts",["backgammon","history of backgammon","board games","tickgammon"],"16:00:00"),
'es':("🦉 Las lecciones de la lechuza · Lección 11, capítulo %d: %s\n%s\nLección completa en YouTube · juega gratis 👉 https://www.tickgammon.com\n#backgammon #juegosdemesa","%s 🦉 La historia del backgammon #shorts",["backgammon","historia del backgammon","juegos de mesa","tickgammon"],"20:00:00")}
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
      i["mediaAltText"]=["Vidéo : la chouette de TickGammon explique « %s » (l'histoire du backgammon)"%t]
      assert len(i["text"])<=280,len(i["text"])
    else: i["providers"]=[{"network":"tiktok"},{"network":"youtube"}]
    assert len(i["youtubeData"]["title"])<=100
    out.append((D[c]+"T"+h+"+01:00",json.dumps(i,ensure_ascii=False)))
json.dump(out,open('metricool11.json','w'),ensure_ascii=False)
print(len(out))

assert all('IA' not in json.loads(x)['text'] and ' AI' not in json.loads(x)['text'] for _,x in out)

bad=__import__('re').compile(r'\b(mise|pari|enjeu|à gagner|commission|rake|cagnotte|apuestas?|stake|money)\b',2)
assert not any(bad.search(x) for _,x in out)

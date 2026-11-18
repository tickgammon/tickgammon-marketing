import json
import sys
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/'+sys.argv[1]+'/videos/lecons/episode12/shorts/lecon12_%s_chap%d_9x16.mp4'
# Leçon 12 : Shorts du 29/03 au 10/04/2027 (pas les vendredis de Friday Cup, ni le dimanche, ni le mercredi de l'annonce)
D=['2027-03-29','2027-03-30','2027-04-01','2027-04-03','2027-04-05','2027-04-06','2027-04-08','2027-04-10']
T={'fr':['Le plateau','Blot, point et ancre','Bloquer','Frapper et rentrer','La course','Le videau','Gammon et backgammon','Match et chouette'],
'en':['The board','Blot, point and anchor','Blocking','Hitting and entering','The race','The doubling cube','Gammon and backgammon','Matches and chouette'],
'es':['El tablero','Blot, punto y ancla','Bloquear','Golpear y entrar','La carrera','El cubo doblador','Gammon y backgammon','Match y chouette']}
H={'fr':["Point, pip, barre, jan intérieur : les mots du plateau.","Blot, point, ancre : qui est fragile, qui est à l'abri ?","Bar point, prime, constructeur : l'art de bloquer.","Frapper un blot, rentrer depuis la barre, tir direct ou indirect.","Course, compte de pips (167 au départ), sortie des pions.","Doubler, prendre ou passer : tout le vocabulaire du videau.","Simple, gammon, backgammon : 1, 2 ou 3 fois la valeur de la partie.","Match, règle de Crawford, ouverture… et la chouette !"],
'en':["Point, pip, bar, home board: the words of the board.","Blot, point, anchor: what's fragile, what's safe?","Bar point, prime, builder: the art of blocking.","Hitting a blot, entering from the bar, direct or indirect shots.","Race, pip count (167 at the start), bearing off.","Double, take or pass: all the doubling cube vocabulary.","Single game, gammon, backgammon: 1, 2 or 3 times the game's value.","Matches, the Crawford rule, the opening… and the chouette!"],
'es':["Punto, pip, barra, cuadrante interior: las palabras del tablero.","Blot, punto, ancla: ¿qué es frágil y qué está a salvo?","Bar point, prime, constructor: el arte de bloquear.","Golpear un blot, entrar desde la barra, tiro directo o indirecto.","Carrera, conteo de pips (167 al principio), sacar las fichas.","Doblar, aceptar o rechazar: todo el vocabulario del cubo.","Simple, gammon, backgammon: 1, 2 o 3 veces el valor de la partida.","Match, regla Crawford, apertura… ¡y la chouette!"]}
S={'fr':("🦉 Les leçons de la chouette · Leçon 12, chapitre %d : %s\n%s\nLeçon complète sur YouTube · jouez gratuitement 👉 https://www.tickgammon.com\n#backgammon #jeudesociete","%s 🦉 Le vocabulaire du joueur #shorts",["backgammon","vocabulaire backgammon","jeu de société","tickgammon"],"12:30:00"),
'en':("🦉 The Owl's Lessons · Lesson 12, chapter %d: %s\n%s\nFull lesson on YouTube · play for free 👉 https://www.tickgammon.com\n#backgammon #boardgames","%s 🦉 The player's vocabulary #shorts",["backgammon","backgammon vocabulary","board games","tickgammon"],"16:00:00"),
'es':("🦉 Las lecciones de la lechuza · Lección 12, capítulo %d: %s\n%s\nLección completa en YouTube · juega gratis 👉 https://www.tickgammon.com\n#backgammon #juegosdemesa","%s 🦉 El vocabulario del jugador #shorts",["backgammon","vocabulario backgammon","juegos de mesa","tickgammon"],"20:00:00")}
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
      i["mediaAltText"]=["Vidéo : la chouette de TickGammon explique « %s » (le vocabulaire du joueur)"%t]
      assert len(i["text"])<=280,len(i["text"])
    else: i["providers"]=[{"network":"tiktok"},{"network":"youtube"}]
    assert len(i["youtubeData"]["title"])<=100
    out.append((D[c]+"T"+h+"+02:00",json.dumps(i,ensure_ascii=False)))
json.dump(out,open('metricool12.json','w'),ensure_ascii=False)
print(len(out))

assert all('IA' not in json.loads(x)['text'] and ' AI' not in json.loads(x)['text'] for _,x in out)

bad=__import__('re').compile(r'\b(mise|pari|enjeu|à gagner|commission|rake|cagnotte|apuestas?|stake|money)\b',2)
assert not any(bad.search(x) for _,x in out)

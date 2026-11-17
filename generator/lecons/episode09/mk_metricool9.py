import json
import sys
R='https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/'+sys.argv[1]+'/videos/lecons/episode09/shorts/lecon9_%s_chap%d_9x16.mp4'
# Leçon 9 : Shorts du 15 au 27/02/2027 (pas les vendredis de Friday Cup, ni le dimanche, ni le mercredi de l'annonce)
D=['2027-02-15','2027-02-16','2027-02-18','2027-02-20','2027-02-22','2027-02-23','2027-02-25','2027-02-27']
T={'fr':['Jouer à plusieurs','Créer un tournoi','Les trois formats','Le jour du tournoi','Clubs et clans','La vie du club','Les cours','Cours particuliers'],
'en':['Playing with others','Creating a tournament','The three formats','Tournament day','Clubs and clans','Club life','Lessons','Private lessons'],
'es':['Jugar en compañía','Crear un torneo','Los tres formatos','El día del torneo','Clubes y clanes','La vida del club','Las clases','Clases particulares']}
H={'fr':["Événements et Cours sur l'accueil, votre club dans votre profil : tout pour jouer à plusieurs.","Ce sont les membres du bureau d'un club ou d'un clan qui créent les tournois.","Élimination directe, toutes rondes ou système suisse : quel format choisir ?","Tournoi en direct : 5 minutes pour rejoindre votre table. Ne soyez pas en retard !","Club ou clan : créez le vôtre et devenez président.","Classement interne, défi du mois, guerre des clans… la vie d'un club.","Des profs validés par TickGammon : Amateur, Expert ou Confirmé.","Un cours rien que pour vous, réponse du prof sous 48 h."],
'en':["Events and Lessons on the home screen, your club in your profile: everything to play together.","Tournaments are created by the board members of a club or a clan.","Direct elimination, round robin or Swiss system: which format to choose?","Live tournament: 5 minutes to join your table. Don't be late!","Club or clan: create your own and become its president.","Internal ranking, monthly challenge, clan war… club life.","Teachers approved by TickGammon: Amateur, Expert or Confirmed.","A lesson just for you, the teacher replies within 48 hours."],
'es':["Eventos y Clases en el inicio, vuestro club en vuestro perfil: todo para jugar en compañía.","Los torneos los crean los miembros de la junta de un club o de un clan.","Eliminación directa, todos contra todos o sistema suizo: ¿qué formato elegir?","Torneo en directo: 5 minutos para uniros a vuestra mesa. ¡No lleguéis tarde!","Club o clan: cread el vuestro y convertíos en presidente.","Clasificación interna, desafío del mes, guerra de clanes… la vida del club.","Profesores validados por TickGammon: Aficionado, Experto o Confirmado.","Una clase solo para vosotros, el profesor responde en 48 horas."]}
S={'fr':("🦉 Les leçons de la chouette · Leçon 9, chapitre %d : %s\n%s\nLeçon complète sur YouTube · jouez gratuitement 👉 https://www.tickgammon.com\n#backgammon #jeudesociete","%s 🦉 Tournois, clubs et cours #shorts",["backgammon","tournoi de backgammon","club de backgammon","tickgammon"],"12:30:00"),
'en':("🦉 The Owl's Lessons · Lesson 9, chapter %d: %s\n%s\nFull lesson on YouTube · play for free 👉 https://www.tickgammon.com\n#backgammon #boardgames","%s 🦉 Tournaments, clubs and lessons #shorts",["backgammon","backgammon tournament","backgammon club","tickgammon"],"16:00:00"),
'es':("🦉 Las lecciones de la lechuza · Lección 9, capítulo %d: %s\n%s\nLección completa en YouTube · juega gratis 👉 https://www.tickgammon.com\n#backgammon #juegosdemesa","%s 🦉 Torneos, clubes y clases #shorts",["backgammon","torneo de backgammon","club de backgammon","tickgammon"],"20:00:00")}
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
      i["mediaAltText"]=["Vidéo : la chouette de TickGammon explique « %s » (tournois, clubs et cours)"%t]
      assert len(i["text"])<=280,len(i["text"])
    else: i["providers"]=[{"network":"tiktok"},{"network":"youtube"}]
    assert len(i["youtubeData"]["title"])<=100
    out.append((D[c]+"T"+h+"+01:00",json.dumps(i,ensure_ascii=False)))
json.dump(out,open('metricool9.json','w'),ensure_ascii=False)
print(len(out))

assert all('IA' not in json.loads(x)['text'] and ' AI' not in json.loads(x)['text'] for _,x in out)

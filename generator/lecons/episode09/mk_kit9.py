# Kit de la leçon 9 (format kit v2) : Actu FR/EN/ES + images + annonce du hub (+ newsletter) + push + ID YouTube.
# Usage : python3 mk_kit9.py <ID_YOUTUBE_11_CARACTERES>  → kit_lecon9.zip
import json, sys, re, zipfile, os
YT = sys.argv[1]
assert re.fullmatch(r'[A-Za-z0-9_-]{11}', YT), 'ID YouTube invalide (11 caractères)'
V = f'https://youtu.be/{YT}'
body = {
'fr': f"""Le backgammon se joue mieux à plusieurs ! Dans la leçon 9 des **Leçons de la chouette**, vous découvrez les tournois, les clubs et les cours de TickGammon.

{V}

## Au programme

- **Jouer à plusieurs** : les boutons Événements et Cours sont sur l'accueil de l'appli ; votre club se trouve dans votre profil.
- **Créer un tournoi** : ce sont les membres du bureau d'un club ou d'un clan (président, vice-président, secrétaire) qui créent les tournois, publics ou privés, avec une inscription gratuite ou en TGC. Tournoi annulé : inscriptions remboursées.
- **Les trois formats** : élimination directe, toutes rondes et système suisse.
- **Le jour du tournoi** : avec date limite par tour, ou en direct, avec 5 minutes pour rejoindre sa table dans les tournois officiels. Et chaque vendredi à 21 h, la Friday Cup !
- **Clubs et clans** : demandez la création du vôtre et devenez président ; fil d'actualité et événements avec rappel la veille.
- **La vie du club** : classement interne, défi du mois, palmarès, guerre des clans entre clubs officiels, et des TGC offerts pour la fidélité.
- **Les cours** : des professeurs validés (Amateur, Expert, Confirmé), un agenda, une liste d'attente, des rappels et des replays.
- **Cours particuliers et profs** : réponse du prof sous 48 h. Les cours payés en TGC, collectifs ou particuliers, sont ouverts à tous ; seuls les cours collectifs gratuits demandent le Pack Sagesse. Et avec le Pack Chouette, vous pouvez devenir professeur.

> Le conseil de la chouette : dans un tournoi en direct, restez près de votre écran : vous n'avez que quelques minutes pour rejoindre votre table !

## Pour aller plus loin

Découvrez notre page [Cours, tournois et clubs](/cours-tournois-clubs-backgammon.php).

La vidéo existe en français, en anglais et en espagnol : choisissez la langue dans ⚙️ → Piste audio. Prochaine leçon le **dimanche 28 février** : le jacquet, le trictrac et le backgammon.""",
'en': f"""Backgammon is better with others! In lesson 9 of **The Owl's Lessons**, you discover TickGammon's tournaments, clubs and lessons.

{V}

## In this lesson

- **Playing with others**: the Events and Lessons buttons are on the app's home screen; your club is in your profile.
- **Creating a tournament**: tournaments are created by the board members of a club or a clan (president, vice-president, secretary), public or private, with free entry or entry in TGC. Cancelled tournament: entries refunded.
- **The three formats**: direct elimination, round robin and the Swiss system.
- **Tournament day**: with a deadline per round, or live, with 5 minutes to join your table in official tournaments. And every Friday at 9 p.m., the Friday Cup!
- **Clubs and clans**: request your own and become its president; news feed and events with a reminder the day before.
- **Club life**: internal ranking, monthly challenge, hall of fame, clan war between official clubs, and free TGC for loyalty.
- **Lessons**: approved teachers (Amateur, Expert, Confirmed), a calendar, a waiting list, reminders and replays.
- **Private lessons and teachers**: the teacher replies within 48 hours. Lessons paid in TGC, group or private, are open to everyone; only free group lessons require the Wisdom Pack. And with the Chouette Pack, you can become a teacher.

> The owl's tip: in a live tournament, stay close to your screen: you only have a few minutes to join your table!

## Going further

Discover our page [Lessons, tournaments and clubs](/cours-tournois-clubs-backgammon.php?lang=en).

The video is available in French, English and Spanish: choose the language in ⚙️ → Audio track. Next lesson on **Sunday 28 February**: jacquet, trictrac and backgammon.""",
'es': f"""¡El backgammon se disfruta más en compañía! En la lección 9 de **Las lecciones de la lechuza**, descubrís los torneos, los clubes y las clases de TickGammon.

{V}

## En esta lección

- **Jugar en compañía**: los botones Eventos y Clases están en el inicio de la app; vuestro club está en vuestro perfil.
- **Crear un torneo**: los crean los miembros de la junta de un club o de un clan (presidente, vicepresidente, secretario), públicos o privados, con inscripción gratuita o en TGC. Torneo cancelado: inscripciones reembolsadas.
- **Los tres formatos**: eliminación directa, todos contra todos y sistema suizo.
- **El día del torneo**: con fecha límite por ronda, o en directo, con 5 minutos para uniros a vuestra mesa en los torneos oficiales. ¡Y cada viernes a las 21 h, la Friday Cup!
- **Clubes y clanes**: pedid la creación del vuestro y convertíos en presidente; muro de noticias y eventos con recordatorio la víspera.
- **La vida del club**: clasificación interna, desafío del mes, palmarés, guerra de clanes entre clubes oficiales y TGC de regalo por fidelidad.
- **Las clases**: profesores validados (Aficionado, Experto, Confirmado), una agenda, lista de espera, recordatorios y grabaciones.
- **Clases particulares y profesores**: el profesor responde en 48 horas. Las clases pagadas en TGC, en grupo o particulares, están abiertas a todos; solo las clases en grupo gratuitas requieren el Pack Sabiduría. Y con el Pack Chouette, podéis haceros profesores.

> El consejo de la lechuza: en un torneo en directo, quedaos cerca de la pantalla: ¡solo tenéis unos minutos para uniros a vuestra mesa!

## Para ir más lejos

Descubrid nuestra página [Clases, torneos y clubes](/cours-tournois-clubs-backgammon.php?lang=es).

El vídeo existe en francés, inglés y español: elegid el idioma en ⚙️ → Pista de audio. Próxima lección el **domingo 28 de febrero**: el jacquet, el trictrac y el backgammon.""",
}
kit = {
 "format": "tickgammon-kit", "format_version": 2,
 "kit_id": "lecon-9-tournois-clubs-cours", "kit_version": 1,
 "title": "Leçon 9 de la chouette : tournois, clubs et cours",
 "type": "lecon",
 "notes": "Sortie dim. 14/02/2027 à 10:30. La vidéo YouTube doit être programmée au 14/02 10:30 avant d'installer ce kit. Les 24 Shorts sont déjà programmés par Claude dans Metricool (15→27/02).",
 "lecon": {"num": 9, "youtube": {"fr": YT, "en": "", "es": ""}},
 "news": [{
  "slug": "lecon-9-tournois-clubs-cours", "category": "conseils", "publish": "2027-02-14 10:30", "pinned": False,
  "title": {"fr": "Leçon 9 de la chouette : tournois, clubs et cours",
            "en": "Owl lesson 9: tournaments, clubs and lessons",
            "es": "Lección 9 de la lechuza: torneos, clubes y clases"},
  "excerpt": {"fr": "Créer un tournoi, choisir son format, rejoindre sa table à temps, faire vivre un club et progresser avec un professeur : la nouvelle leçon vidéo de la chouette.",
              "en": "Creating a tournament, choosing its format, joining your table on time, bringing a club to life and improving with a teacher: the owl's new video lesson.",
              "es": "Crear un torneo, elegir su formato, llegar a tiempo a la mesa, dar vida a un club y progresar con un profesor: la nueva lección en vídeo de la lechuza."},
  "body": body,
  "image": {"fr": "actu_fr.jpg", "en": "actu_en.jpg", "es": "actu_es.jpg"},
  "announce": {"active": True, "starts_at": None, "ends_at": "2027-02-27 23:59", "popup": True, "banner": True,
               "audience": "all", "color": "#c9954a", "emoji": "🦉", "newsletter": True,
               "title": {}, "text": {}, "btn": {"fr": "Voir la leçon", "en": "Watch the lesson", "es": "Ver la lección"},
               "image": {"fr": "actu_fr.jpg", "en": "actu_en.jpg", "es": "actu_es.jpg"}}
 }],
 "push": [{"ref": "lecon9-sortie", "send_at": "2027-02-14 18:00",
           "title": {"fr": "🦉 Leçon 9 : tournois, clubs et cours", "en": "🦉 Lesson 9: tournaments, clubs and lessons", "es": "🦉 Lección 9: torneos, clubes y clases"},
           "body": {"fr": "Tournois, clubs et cours expliqués par la chouette.", "en": "Tournaments, clubs and lessons explained by the owl.", "es": "Torneos, clubes y clases explicados por la lechuza."},
           "url": "/actu.php?a=lecon-9-tournois-clubs-cours"}],
 "metricool": json.load(open('metricool_kit.json')) if os.path.exists('metricool_kit.json') else []
}
bad = re.compile(r'\b(mise|pari|enjeu|à gagner|commission|rake|cagnotte|apuestas?|stake|money)\b', re.I)
txt = json.dumps(kit, ensure_ascii=False)
assert not bad.search(txt), bad.search(txt)
os.makedirs('kit', exist_ok=True)
with zipfile.ZipFile('kit_lecon9.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('kit.json', json.dumps(kit, ensure_ascii=False, indent=1))
    for L, s in (('fr', ''), ('en', '_en'), ('es', '_es')):
        z.write(f'miniature_lecon9_tournois{s}.jpg', f'images/actu_{L}.jpg')
print('kit_lecon9.zip OK', YT)

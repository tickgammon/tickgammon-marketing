# Kit de la leçon 11 (format kit v2) : Actu FR/EN/ES + images + annonce du hub (+ newsletter) + push + ID YouTube.
# Usage (depuis le dossier qui contient les 3 miniatures miniature_lecon11_histoire*.jpg) :
#   python3 mk_kit11.py <ID_YOUTUBE_11_CARACTERES>  → kit_lecon11.zip
import json, sys, re, zipfile, os
YT = sys.argv[1]
assert re.fullmatch(r'[A-Za-z0-9_-]{11}', YT), 'ID YouTube invalide (11 caractères)'
IMG = [f'miniature_lecon11_histoire{s}.jpg' for s in ('', '_en', '_es')]
for f in IMG: assert os.path.exists(f), f'image manquante : {f} (lancer le script depuis le dossier des miniatures)'
V = f'https://youtu.be/{YT}'
body = {
'fr': f"""Le backgammon est l'un des plus vieux jeux de plateau encore joués. Dans la leçon 11 des **Leçons de la chouette**, on remonte le temps : un voyage de plusieurs milliers d'années !

{V}

## Au programme

- **Les lointains ancêtres** : le jeu royal d'Ur, il y a environ 4 500 ans en Mésopotamie, et le senet égyptien : déjà des courses de pions au rythme des dés.
- **Rome : la tabula** : 24 cases, 15 pions par joueur et des pions isolés qu'on frappe. La partie de l'empereur Zénon, au Ve siècle, se jouait avec trois dés !
- **La Perse et le nard** : la légende du sage Bozorgmehr, racontée par le poète Ferdowsi, et le nard (nardy), toujours très joué aujourd'hui.
- **Le Moyen Âge** : les jeux de tables partout en Europe, et le grand livre des jeux d'Alphonse X de Castille en 1283.
- **Le nom « backgammon »** : apparu en Angleterre au XVIIe siècle ; le traité d'Edmond Hoyle en 1743 ; le trictrac et le jacquet en France.
- **Le videau et l'âge d'or** : l'invention du videau à New York dans les années 1920, les grands tournois des années 1960-1970 et le championnat du monde à Monte-Carlo.
- **Les ordinateurs** : TD-Gammon au début des années 1990, puis GNU Backgammon, gratuit et libre.
- **Aujourd'hui : en ligne** : jouer à toute heure contre des joueurs du monde entier, analyser ses coups, suivre des cours et participer à des tournois.

> Le conseil de la chouette : à chaque partie, vous jouez à un jeu que des générations de joueurs ont aimé avant vous. Les mêmes quinze pions, les mêmes deux dés !

## Pour aller plus loin

Découvrez notre page [L'histoire du backgammon](/histoire-backgammon.php).

La vidéo existe en français, en anglais et en espagnol : choisissez la langue dans ⚙️ → Piste audio. Prochaine leçon le **dimanche 28 mars** : le vocabulaire du joueur, la dernière leçon de la saison.""",
'en': f"""Backgammon is one of the oldest board games still played. In lesson 11 of **The Owl's Lessons**, we go back in time: a journey of several thousand years!

{V}

## In this lesson

- **Distant ancestors**: the Royal Game of Ur, about 4,500 years ago in Mesopotamia, and Egyptian senet: already races of pieces to the rhythm of the dice.
- **Rome: tabula**: 24 points, 15 checkers per player and lone checkers that get hit. Emperor Zeno's game, in the 5th century, was played with three dice!
- **Persia and nard**: the legend of the sage Bozorgmehr, told by the poet Ferdowsi, and nard (nardy), still widely played today.
- **The Middle Ages**: tables games all over Europe, and the great book of games of Alfonso X of Castile in 1283.
- **The name "backgammon"**: it appears in England in the 17th century; Edmond Hoyle's treatise in 1743; trictrac and jacquet in France.
- **The cube and the golden age**: the invention of the doubling cube in New York in the 1920s, the great tournaments of the 1960s and 1970s and the world championship in Monte Carlo.
- **Computers**: TD-Gammon in the early 1990s, then GNU Backgammon, free and open source.
- **Today: online**: play at any time against players from all over the world, analyse your moves, take lessons and join tournaments.

> The owl's tip: every game you play is a game that generations of players loved before you. The same fifteen checkers, the same two dice!

## Learn more

Discover our page [The history of backgammon](/histoire-backgammon.php?lang=en).

The video is available in French, English and Spanish: choose the language in ⚙️ → Audio track. Next lesson on **Sunday 28 March**: the player's vocabulary, the last lesson of the season.""",
'es': f"""El backgammon es uno de los juegos de tablero más antiguos que todavía se juegan. En la lección 11 de **Las lecciones de la lechuza**, viajamos en el tiempo: ¡un viaje de varios miles de años!

{V}

## En esta lección

- **Los lejanos antepasados**: el juego real de Ur, hace unos 4500 años en Mesopotamia, y el senet egipcio: ya carreras de piezas al ritmo de los dados.
- **Roma: la tabula**: 24 casillas, 15 fichas por jugador y fichas sueltas que se golpean. ¡La partida del emperador Zenón, en el siglo V, se jugaba con tres dados!
- **Persia y el nard**: la leyenda del sabio Bozorgmehr, contada por el poeta Ferdousí, y el nard (nardy), que se sigue jugando mucho hoy.
- **La Edad Media**: los juegos de tablas por toda Europa, y el gran libro de juegos de Alfonso X de Castilla en 1283.
- **El nombre «backgammon»**: aparece en Inglaterra en el siglo XVII; el tratado de Edmond Hoyle en 1743; el trictrac y el jacquet en Francia.
- **El cubo y la edad de oro**: el invento del cubo doblador en Nueva York en los años 1920, los grandes torneos de los años 1960 y 1970 y el campeonato del mundo en Montecarlo.
- **Los ordenadores**: TD-Gammon a principios de los años 1990, y después GNU Backgammon, gratuito y libre.
- **Hoy: en línea**: jugar a cualquier hora contra jugadores de todo el mundo, analizar vuestras jugadas, seguir clases y participar en torneos.

> El consejo de la lechuza: en cada partida, jugáis a un juego que generaciones de jugadores amaron antes que vosotros. ¡Las mismas quince fichas, los mismos dos dados!

## Para saber más

Descubrid nuestra página [La historia del backgammon](/histoire-backgammon.php?lang=es).

El vídeo existe en francés, inglés y español: elegid el idioma en ⚙️ → Pista de audio. Próxima lección el **domingo 28 de marzo**: el vocabulario del jugador, la última lección de la temporada.""",
}
kit = {
 "format": "tickgammon-kit", "format_version": 2,
 "kit_id": "lecon-11-histoire-backgammon", "kit_version": 1,
 "title": "Leçon 11 de la chouette : l'histoire du backgammon",
 "type": "lecon",
 "notes": "Sortie dim. 14/03/2027 à 10:30. La vidéo YouTube doit être programmée au 14/03 10:30 avant d'installer ce kit. Les 24 Shorts sont déjà programmés par Claude dans Metricool (15→27/03).",
 "lecon": {"num": 11, "youtube": {"fr": YT, "en": "", "es": ""}},
 "news": [{
  "slug": "lecon-11-histoire-backgammon", "category": "conseils", "publish": "2027-03-14 10:30", "pinned": False,
  "title": {"fr": "Leçon 11 de la chouette : l'histoire du backgammon",
            "en": "Owl lesson 11: the history of backgammon",
            "es": "Lección 11 de la lechuza: la historia del backgammon"},
  "excerpt": {"fr": "Du jeu royal d'Ur aux ordinateurs : la chouette vous raconte 4 500 ans d'histoire du backgammon.",
              "en": "From the Royal Game of Ur to computers: the owl tells you 4,500 years of backgammon history.",
              "es": "Del juego real de Ur a los ordenadores: la lechuza os cuenta 4500 años de historia del backgammon."},
  "body": body,
  "image": {"fr": "actu_fr.jpg", "en": "actu_en.jpg", "es": "actu_es.jpg"},
  "announce": {"active": True, "starts_at": None, "ends_at": "2027-03-27 23:59", "popup": True, "banner": True,
               "audience": "all", "color": "#c9954a", "emoji": "🦉", "newsletter": True,
               "title": {}, "text": {}, "btn": {"fr": "Voir la leçon", "en": "Watch the lesson", "es": "Ver la lección"},
               "image": {"fr": "actu_fr.jpg", "en": "actu_en.jpg", "es": "actu_es.jpg"}}
 }],
 "push": [{"ref": "lecon11-sortie", "send_at": "2027-03-14 18:00",
           "title": {"fr": "🦉 Leçon 11 : l'histoire du backgammon", "en": "🦉 Lesson 11: the history of backgammon", "es": "🦉 Lección 11: la historia del backgammon"},
           "body": {"fr": "4 500 ans d'histoire, du jeu d'Ur à Monte-Carlo : la chouette vous raconte.", "en": "4,500 years of history, from Ur to Monte Carlo: the owl tells you.", "es": "4500 años de historia, de Ur a Montecarlo: la lechuza os lo cuenta."},
           "url": "/actu.php?a=lecon-11-histoire-backgammon"}],
 "metricool": []
}
bad = re.compile(r'\b(mise|pari|enjeu|à gagner|commission|rake|cagnotte|apuestas?|stake|money)\b', re.I)
txt = json.dumps(kit, ensure_ascii=False)
assert not bad.search(txt), bad.search(txt)
with zipfile.ZipFile('kit_lecon11.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('kit.json', json.dumps(kit, ensure_ascii=False, indent=1))
    for L, f in zip(('fr', 'en', 'es'), IMG):
        z.write(f, f'images/actu_{L}.jpg')
print('kit_lecon11.zip OK', YT)

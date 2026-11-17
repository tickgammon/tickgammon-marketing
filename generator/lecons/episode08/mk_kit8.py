# Kit de la leçon 8 (format kit v2) : Actu FR/EN/ES + images + annonce du hub (+ newsletter) + push + ID YouTube.
# Usage : python3 mk_kit8.py <ID_YOUTUBE_11_CARACTERES>  → kit_lecon8.zip
import json, sys, re, zipfile, os
YT = sys.argv[1]
assert re.fullmatch(r'[A-Za-z0-9_-]{11}', YT), 'ID YouTube invalide (11 caractères)'
V = f'https://youtu.be/{YT}'
body = {
'fr': f"""Jouer contre de vrais joueurs, c'est là que le backgammon devient passionnant… et que tout le monde regarde le même chiffre : l'ELO. Dans la leçon 8 des **Leçons de la chouette**, vous apprenez à jouer en ligne et à faire grimper votre classement.

{V}

## Au programme

- **Jouer en ligne** : un compte gratuit, le même dans le navigateur, sur Android et sur Windows.
- **Formats et rythmes** : le nombre de points du match, et quatre rythmes : Zen, Classique, Blitz et Bullet.
- **Vos amis** : les défier même hors ligne (ils reçoivent une notification) et regarder leurs parties.
- **L'ELO** : tout le monde commence à 1500 ; chaque partie contre un vrai joueur le fait monter ou descendre.
- **Comment l'ELO bouge** : battre plus fort que soi rapporte plus, perdre contre plus faible coûte cher.
- **L'expérience** : l'ELO bouge beaucoup pendant les 50 premières parties, puis se stabilise.
- **Le classement** : votre rang, votre ELO, vos victoires et défaites, et des paliers à débloquer : Élite (1600), Maître (1800), Légende (2100).
- **Quatre conseils** : jouer régulièrement, faire une pause après une défaite, choisir des adversaires de son niveau ou un peu plus forts, et utiliser tout ce que vous avez appris.
- **Le videau en ligne** : en match, il change tout. Pensez à la règle des 25 %, et relisez vos décisions dans l'analyse.

> Le conseil de la chouette : battez des joueurs plus forts que vous, c'est comme ça que l'ELO grimpe le plus vite !

## Pour aller plus loin

Découvrez notre page [Jouer au backgammon en ligne](/jouer-backgammon-en-ligne.php). C'est gratuit, dans votre navigateur, sur Android et sur Windows. Sur TickGammon, tout reste un jeu : les TGC sont une monnaie de jeu offerte toutes les 12 heures, qui ne se retire pas et ne se convertit pas.

La vidéo existe en français, en anglais et en espagnol : choisissez la langue dans ⚙️ → Piste audio. Prochaine leçon le **dimanche 14 février** : les tournois, les clubs et les cours.""",
'en': f"""Playing against real players is where backgammon gets exciting… and where everyone watches the same number: the ELO rating. In lesson 8 of **The Owl's Lessons**, you learn how to play online and make your ranking climb.

{V}

## In this lesson

- **Playing online**: a free account, the same in your browser, on Android and on Windows.
- **Formats and speeds**: the match length, and four paces: Zen, Classic, Blitz and Bullet.
- **Your friends**: challenge them even when they're offline (they get a notification) and watch their games.
- **ELO**: everyone starts at 1500; every game against a real player makes it go up or down.
- **How ELO moves**: beating a stronger player brings more, losing to a weaker one costs a lot.
- **Experience**: your rating moves a lot during your first 50 games, then settles down.
- **The ranking**: your rank, your rating, your wins and losses, and milestones to unlock: Elite (1600), Master (1800), Legend (2100).
- **Four tips**: play regularly, take a break after a loss, choose opponents at your level or slightly stronger, and use everything you've learned.
- **The cube online**: in a match, it changes everything. Remember the 25% rule, and review your decisions in the analysis.

> The owl's tip: beat players stronger than you, that's how your rating climbs fastest!

## Going further

Discover our page [Play backgammon online](/jouer-backgammon-en-ligne.php?lang=en). It's free, in your browser, on Android and on Windows. On TickGammon, it's all just a game: TGC are an in-game currency offered every 12 hours, which can't be withdrawn or converted.

The video is available in French, English and Spanish: choose the language in ⚙️ → Audio track. Next lesson on **Sunday 14 February**: tournaments, clubs and lessons.""",
'es': f"""Jugar contra jugadores reales es cuando el backgammon se vuelve apasionante… y cuando todo el mundo mira el mismo número: el ELO. En la lección 8 de **Las lecciones de la lechuza**, aprendéis a jugar en línea y a hacer subir vuestra clasificación.

{V}

## En esta lección

- **Jugar en línea**: una cuenta gratuita, la misma en el navegador, en Android y en Windows.
- **Formatos y ritmos**: los puntos del match y cuatro ritmos: Zen, Clásico, Blitz y Bullet.
- **Vuestros amigos**: desafiadlos aunque no estén conectados (reciben una notificación) y ved sus partidas.
- **El ELO**: todo el mundo empieza con 1500; cada partida contra un jugador real lo hace subir o bajar.
- **Cómo se mueve el ELO**: ganar a alguien más fuerte da más, perder contra alguien más débil sale caro.
- **La experiencia**: el ELO se mueve mucho durante las 50 primeras partidas, y luego se estabiliza.
- **La clasificación**: vuestro puesto, vuestro ELO, victorias y derrotas, y niveles por desbloquear: Élite (1600), Maestro (1800), Leyenda (2100).
- **Cuatro consejos**: jugar con regularidad, hacer una pausa tras una derrota, elegir adversarios de vuestro nivel o un poco más fuertes, y usar todo lo aprendido.
- **El cubo en línea**: en un match lo cambia todo. Pensad en la regla del 25 %, y revisad vuestras decisiones en el análisis.

> El consejo de la lechuza: ¡ganad a jugadores más fuertes que vosotros, así es como el ELO sube más rápido!

## Para ir más lejos

Descubrid nuestra página [Jugar al backgammon en línea](/jouer-backgammon-en-ligne.php?lang=es). Es gratis, en el navegador, en Android y en Windows. En TickGammon, todo es un juego: los TGC son una moneda de juego regalada cada 12 horas, que no se puede retirar ni convertir.

El vídeo existe en francés, inglés y español: elegid el idioma en ⚙️ → Pista de audio. Próxima lección el **domingo 14 de febrero**: los torneos, los clubes y las clases.""",
}
kit = {
 "format": "tickgammon-kit", "format_version": 2,
 "kit_id": "lecon-8-jouer-en-ligne", "kit_version": 1,
 "title": "Leçon 8 de la chouette : jouer en ligne, classement et ELO",
 "type": "lecon",
 "notes": "Sortie dim. 31/01/2027 à 10:30. La vidéo YouTube doit être programmée au 31/01 10:30 avant d'installer ce kit. Les 24 Shorts sont déjà programmés par Claude dans Metricool (1→11/02).",
 "lecon": {"num": 8, "youtube": {"fr": YT, "en": "", "es": ""}},
 "news": [{
  "slug": "lecon-8-jouer-en-ligne", "category": "conseils", "publish": "2027-01-31 10:30", "pinned": False,
  "title": {"fr": "Leçon 8 de la chouette : jouer en ligne, le classement et l'ELO",
            "en": "Owl lesson 8: playing online, rankings and ELO",
            "es": "Lección 8 de la lechuza: jugar en línea, la clasificación y el ELO"},
  "excerpt": {"fr": "Comment se calcule l'ELO, comment il bouge et comment le faire grimper : dans sa nouvelle leçon vidéo, la chouette vous emmène jouer en ligne contre de vrais joueurs.",
              "en": "How the ELO rating is calculated, how it moves and how to make it climb: in her new video lesson, the owl takes you online to play against real players.",
              "es": "Cómo se calcula el ELO, cómo se mueve y cómo hacerlo subir: en su nueva lección en vídeo, la lechuza os lleva a jugar en línea contra jugadores reales."},
  "body": body,
  "image": {"fr": "actu_fr.jpg", "en": "actu_en.jpg", "es": "actu_es.jpg"},
  "announce": {"active": True, "starts_at": None, "ends_at": "2027-02-13 23:59", "popup": True, "banner": True,
               "audience": "all", "color": "#c9954a", "emoji": "🦉", "newsletter": True,
               "title": {}, "text": {}, "btn": {"fr": "Voir la leçon", "en": "Watch the lesson", "es": "Ver la lección"},
               "image": {"fr": "actu_fr.jpg", "en": "actu_en.jpg", "es": "actu_es.jpg"}}
 }],
 "push": [{"ref": "lecon8-sortie", "send_at": "2027-01-31 18:00",
           "title": {"fr": "🦉 Leçon 8 : faites grimper votre ELO", "en": "🦉 Lesson 8: make your rating climb", "es": "🦉 Lección 8: haced subir vuestro ELO"},
           "body": {"fr": "Jouer en ligne, le classement et l'ELO expliqués par la chouette.", "en": "Playing online, rankings and the ELO rating explained by the owl.", "es": "Jugar en línea, la clasificación y el ELO explicados por la lechuza."},
           "url": "/actu.php?a=lecon-8-jouer-en-ligne"}],
 "metricool": json.load(open('metricool_kit.json')) if os.path.exists('metricool_kit.json') else []
}
bad = re.compile(r'\b(mise|pari|enjeu|à gagner|commission|rake|cagnotte|apuestas?|stake|money)\b', re.I)
txt = json.dumps(kit, ensure_ascii=False)
assert not bad.search(txt), bad.search(txt)
os.makedirs('kit', exist_ok=True)
with zipfile.ZipFile('kit_lecon8.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('kit.json', json.dumps(kit, ensure_ascii=False, indent=1))
    for L, s in (('fr', ''), ('en', '_en'), ('es', '_es')):
        z.write(f'miniature_lecon8_elo{s}.jpg', f'images/actu_{L}.jpg')
print('kit_lecon8.zip OK', YT)

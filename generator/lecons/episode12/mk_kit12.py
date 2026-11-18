# Kit de la leçon 12 (format kit v2) : Actu FR/EN/ES + images + annonce du hub (+ newsletter) + push + ID YouTube.
# Usage (depuis le dossier qui contient les 3 miniatures miniature_lecon12_vocabulaire*.jpg) :
#   python3 mk_kit12.py <ID_YOUTUBE_11_CARACTERES>  → kit_lecon12.zip
import json, sys, re, zipfile, os
YT = sys.argv[1]
assert re.fullmatch(r'[A-Za-z0-9_-]{11}', YT), 'ID YouTube invalide (11 caractères)'
IMG = [f'miniature_lecon12_vocabulaire{s}.jpg' for s in ('', '_en', '_es')]
for f in IMG: assert os.path.exists(f), f'image manquante : {f} (lancer le script depuis le dossier des miniatures)'
V = f'https://youtu.be/{YT}'
body = {
'fr': f"""Blot, prime, gammon, videau… Dans la leçon 12 des **Leçons de la chouette**, la dernière de la saison 1, vous apprenez tous les mots du joueur de backgammon. À la fin, vous parlerez backgammon comme un habitué du club !

{V}

## Au programme

- **Le plateau** : les 24 points (ou flèches), le pip, la barre, le jan intérieur et le jan extérieur.
- **Blot, point et ancre** : un pion seul est un blot, fragile ; avec deux pions, vous faites un point ; un point tenu chez l'adversaire est une ancre.
- **Bloquer** : le bar point, le prime (six points d'affilée : personne ne passe !) et le constructeur.
- **Frapper et rentrer** : le pion frappé va sur la barre et doit rentrer avant tout autre coup ; tir direct ou tir indirect.
- **La course** : le compte de pips (167 au départ pour chacun) et la sortie des pions.
- **Le videau** : doubler la valeur de la partie, prendre ou passer.
- **Gammon et backgammon** : une victoire simple, double ou triple.
- **Match et chouette** : le match en points, la règle de Crawford, l'ouverture, et la chouette, le backgammon à trois joueurs ou plus.

> Le conseil de la chouette : pour retrouver tous ces mots à tout moment, gardez notre lexique sous la main !

## Pour aller plus loin

Découvrez notre page [Le lexique du backgammon](/lexique-backgammon.php).

La vidéo existe en français, en anglais et en espagnol : choisissez la langue dans ⚙️ → Piste audio. Cette leçon termine la **saison 1** des Leçons de la chouette : merci de l'avoir suivie ! La saison 2 arrive bientôt.""",
'en': f"""Blot, prime, gammon, doubling cube… In lesson 12 of **The Owl's Lessons**, the last one of season 1, you learn every word a backgammon player uses. By the end, you'll talk backgammon like a club regular!

{V}

## In this lesson

- **The board**: the 24 points, the pip, the bar, the home board and the outer board.
- **Blot, point and anchor**: a single checker is a blot, fragile; with two checkers you make a point; a point held in your opponent's home board is an anchor.
- **Blocking**: the bar point, the prime (six points in a row: nobody gets past!) and the builder.
- **Hitting and entering**: the hit checker goes to the bar and must enter before any other move; direct and indirect shots.
- **The race**: the pip count (167 each at the start) and bearing off.
- **The doubling cube**: doubling the value of the game, take or pass.
- **Gammon and backgammon**: a single, double or triple win.
- **Matches and chouette**: matches to a number of points, the Crawford rule, the opening, and the chouette, backgammon for three or more players.

> The owl's tip: to find all these words at any time, keep our glossary close at hand!

## Learn more

Discover our page [The backgammon glossary](/lexique-backgammon.php?lang=en).

The video is available in French, English and Spanish: choose the language in ⚙️ → Audio track. This lesson ends **season 1** of The Owl's Lessons: thank you for following it! Season 2 is coming soon.""",
'es': f"""Blot, prime, gammon, cubo doblador… En la lección 12 de **Las lecciones de la lechuza**, la última de la temporada 1, aprendéis todas las palabras del jugador de backgammon. ¡Al final, hablaréis de backgammon como un habitual del club!

{V}

## En esta lección

- **El tablero**: los 24 puntos (o puntas), el pip, la barra, el cuadrante interior y el cuadrante exterior.
- **Blot, punto y ancla**: una ficha sola es un blot, frágil; con dos fichas hacéis un punto; un punto que tenéis en el campo del adversario es un ancla.
- **Bloquear**: el bar point, el prime (seis puntos seguidos: ¡nadie pasa!) y el constructor.
- **Golpear y entrar**: la ficha golpeada va a la barra y debe entrar antes de cualquier otra jugada; tiro directo o indirecto.
- **La carrera**: el conteo de pips (167 para cada uno al principio) y sacar las fichas.
- **El cubo doblador**: doblar el valor de la partida, aceptar o rechazar.
- **Gammon y backgammon**: una victoria simple, doble o triple.
- **Match y chouette**: el match a puntos, la regla Crawford, la apertura, y la chouette, el backgammon para tres jugadores o más.

> El consejo de la lechuza: para encontrar todas estas palabras en cualquier momento, ¡tened nuestro glosario a mano!

## Para saber más

Descubrid nuestra página [El glosario del backgammon](/lexique-backgammon.php?lang=es).

El vídeo existe en francés, inglés y español: elegid el idioma en ⚙️ → Pista de audio. Esta lección cierra la **temporada 1** de Las lecciones de la lechuza: ¡gracias por seguirla! La temporada 2 llega pronto.""",
}
kit = {
 "format": "tickgammon-kit", "format_version": 2,
 "kit_id": "lecon-12-vocabulaire-joueur", "kit_version": 1,
 "title": "Leçon 12 de la chouette : le vocabulaire du joueur",
 "type": "lecon",
 "notes": "Sortie dim. 28/03/2027 à 10:30. La vidéo YouTube doit être programmée au 28/03 10:30 avant d'installer ce kit. Les 24 Shorts sont déjà programmés par Claude dans Metricool (29/03→10/04).",
 "lecon": {"num": 12, "youtube": {"fr": YT, "en": "", "es": ""}},
 "news": [{
  "slug": "lecon-12-vocabulaire-joueur", "category": "conseils", "publish": "2027-03-28 10:30", "pinned": False,
  "title": {"fr": "Leçon 12 de la chouette : le vocabulaire du joueur",
            "en": "Owl lesson 12: the player's vocabulary",
            "es": "Lección 12 de la lechuza: el vocabulario del jugador"},
  "excerpt": {"fr": "Blot, prime, gammon, videau : la chouette vous apprend tous les mots du joueur de backgammon.",
              "en": "Blot, prime, gammon, doubling cube: the owl teaches you every word a backgammon player uses.",
              "es": "Blot, prime, gammon, cubo doblador: la lechuza os enseña todas las palabras del jugador de backgammon."},
  "body": body,
  "image": {"fr": "actu_fr.jpg", "en": "actu_en.jpg", "es": "actu_es.jpg"},
  "announce": {"active": True, "starts_at": None, "ends_at": "2027-04-10 23:59", "popup": True, "banner": True,
               "audience": "all", "color": "#c9954a", "emoji": "🦉", "newsletter": True,
               "title": {}, "text": {}, "btn": {"fr": "Voir la leçon", "en": "Watch the lesson", "es": "Ver la lección"},
               "image": {"fr": "actu_fr.jpg", "en": "actu_en.jpg", "es": "actu_es.jpg"}}
 }],
 "push": [{"ref": "lecon12-sortie", "send_at": "2027-03-28 18:00",
           "title": {"fr": "🦉 Leçon 12 : le vocabulaire du joueur", "en": "🦉 Lesson 12: the player's vocabulary", "es": "🦉 Lección 12: el vocabulario del jugador"},
           "body": {"fr": "Blot, prime, gammon… parlez backgammon comme un habitué !", "en": "Blot, prime, gammon… talk backgammon like a regular!", "es": "Blot, prime, gammon… ¡habla backgammon como un habitual!"},
           "url": "/actu.php?a=lecon-12-vocabulaire-joueur"}],
 "metricool": []
}
bad = re.compile(r'\b(mise|pari|enjeu|à gagner|commission|rake|cagnotte|apuestas?|stake|money)\b', re.I)
txt = json.dumps(kit, ensure_ascii=False)
assert not bad.search(txt), bad.search(txt)
with zipfile.ZipFile('kit_lecon12.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('kit.json', json.dumps(kit, ensure_ascii=False, indent=1))
    for L, f in zip(('fr', 'en', 'es'), IMG):
        z.write(f, f'images/actu_{L}.jpg')
print('kit_lecon12.zip OK', YT)

# Kit de la leçon 10 (format kit v2) : Actu FR/EN/ES + images + annonce du hub (+ newsletter) + push + ID YouTube.
# Usage (depuis le dossier qui contient les 3 miniatures miniature_lecon10_jacquet_trictrac*.jpg) :
#   python3 mk_kit10.py <ID_YOUTUBE_11_CARACTERES>  → kit_lecon10.zip
import json, sys, re, zipfile, os
YT = sys.argv[1]
assert re.fullmatch(r'[A-Za-z0-9_-]{11}', YT), 'ID YouTube invalide (11 caractères)'
IMG = [f'miniature_lecon10_jacquet_trictrac{s}.jpg' for s in ('', '_en', '_es')]
for f in IMG: assert os.path.exists(f), f'image manquante : {f} (lancer le script depuis le dossier des miniatures)'
V = f'https://youtu.be/{YT}'
body = {
'fr': f"""« On fait un trictrac ? » Jacquet, trictrac, backgammon… est-ce le même jeu ? Dans la leçon 10 des **Leçons de la chouette**, vous apprenez à les reconnaître.

{V}

## Au programme

- **Une seule famille** : les jeux de tables, joués en Europe depuis l'Antiquité romaine, sur un plateau qui se replie, le tablier.
- **Le même matériel** : 15 pions chacun, deux dés et un plateau de 24 flèches.
- **Le backgammon** : sens opposés, départ sur quatre flèches, un pion seul peut être frappé, et le videau double la valeur de la partie.
- **Le jacquet : le départ** : 15 pions empilés sur une seule flèche, et les deux joueurs tournent dans le même sens.
- **Le jacquet : bloquer** : on ne frappe jamais, un seul pion bloque une flèche ; pas de videau. Les règles de détail varient selon les familles.
- **Le trictrac** : le grand jeu des XVIIe et XVIIIe siècles, où l'on gagne en marquant des points, comptés avec des jetons et des fiches.
- **Le mot « trictrac »** : grâce à son prestige, il a désigné le plateau, puis le backgammon lui-même.
- **En résumé** : un tableau pour tout comparer.

> Le conseil de la chouette : si vous connaissez le jacquet, le backgammon vous paraîtra vite familier : même plateau, mêmes dés, même logique de course.

## Pour aller plus loin

Découvrez notre page [Jacquet, trictrac et backgammon](/jacquet-trictrac-backgammon.php).

La vidéo existe en français, en anglais et en espagnol : choisissez la langue dans ⚙️ → Piste audio. Prochaine leçon le **dimanche 14 mars** : l'histoire du backgammon.""",
'en': f""""Shall we play a trictrac?" Jacquet, trictrac, backgammon… are they the same game? In lesson 10 of **The Owl's Lessons**, you learn to tell them apart.

{V}

## In this lesson

- **One family**: the tables games, played in Europe since Roman times, on a folding board the French call a "tablier".
- **The same equipment**: 15 checkers each, two dice and a board with 24 points.
- **Backgammon**: opposite directions, a start on four points, a single checker can be hit, and the doubling cube doubles the value of the game.
- **Jacquet: the start**: 15 checkers stacked on a single point, and both players go round in the same direction.
- **Jacquet: blocking**: you never hit, a single checker blocks a point; no doubling cube. The finer rules vary between families.
- **Trictrac**: the great game of 17th- and 18th-century France, where you win by scoring points, counted with tokens and pegs.
- **The word "trictrac"**: thanks to its prestige, it came to mean the board, and then backgammon itself.
- **In short**: a table to compare everything.

> The owl's tip: if you know jacquet, backgammon will soon feel familiar: same board, same dice, same racing logic.

## Going further

Discover our page [Jacquet, trictrac and backgammon](/jacquet-trictrac-backgammon.php?lang=en).

The video is available in French, English and Spanish: choose the language in ⚙️ → Audio track. Next lesson on **Sunday 14 March**: the history of backgammon.""",
'es': f"""«¿Echamos un trictrac?» Jacquet, trictrac, backgammon… ¿son el mismo juego? En la lección 10 de **Las lecciones de la lechuza**, aprendéis a distinguirlos.

{V}

## En esta lección

- **Una sola familia**: los juegos de tablas, jugados en Europa desde la Antigüedad romana, en un tablero que se pliega, el «tablier».
- **El mismo material**: 15 fichas cada uno, dos dados y un tablero de 24 puntas.
- **El backgammon**: sentidos opuestos, salida en cuatro puntas, una ficha sola puede ser golpeada, y el cubo dobla el valor de la partida.
- **El jacquet: la salida**: 15 fichas apiladas en una sola punta, y los dos jugadores giran en el mismo sentido.
- **El jacquet: bloquear**: nunca se golpea, una sola ficha bloquea una punta; no hay cubo. Las reglas de detalle cambian según las familias.
- **El trictrac**: el gran juego de la Francia de los siglos XVII y XVIII, donde se gana marcando puntos, contados con fichas y clavijas.
- **La palabra «trictrac»**: gracias a su prestigio, pasó a designar el tablero y luego el propio backgammon.
- **En resumen**: una tabla para compararlo todo.

> El consejo de la lechuza: si conocéis el jacquet, el backgammon os resultará familiar enseguida: mismo tablero, mismos dados, misma lógica de carrera.

## Para ir más lejos

Descubrid nuestra página [Jacquet, trictrac y backgammon](/jacquet-trictrac-backgammon.php?lang=es).

El vídeo existe en francés, inglés y español: elegid el idioma en ⚙️ → Pista de audio. Próxima lección el **domingo 14 de marzo**: la historia del backgammon.""",
}
kit = {
 "format": "tickgammon-kit", "format_version": 2,
 "kit_id": "lecon-10-jacquet-trictrac-backgammon", "kit_version": 1,
 "title": "Leçon 10 de la chouette : jacquet, trictrac et backgammon",
 "type": "lecon",
 "notes": "Sortie dim. 28/02/2027 à 10:30. La vidéo YouTube doit être programmée au 28/02 10:30 avant d'installer ce kit. Les 24 Shorts sont déjà programmés par Claude dans Metricool (1→13/03).",
 "lecon": {"num": 10, "youtube": {"fr": YT, "en": "", "es": ""}},
 "news": [{
  "slug": "lecon-10-jacquet-trictrac-backgammon", "category": "conseils", "publish": "2027-02-28 10:30", "pinned": False,
  "title": {"fr": "Leçon 10 de la chouette : jacquet, trictrac et backgammon",
            "en": "Owl lesson 10: jacquet, trictrac and backgammon",
            "es": "Lección 10 de la lechuza: jacquet, trictrac y backgammon"},
  "excerpt": {"fr": "Jacquet, trictrac, backgammon : même famille, même plateau… mais pas le même jeu. La chouette vous apprend à les reconnaître.",
              "en": "Jacquet, trictrac, backgammon: same family, same board… but not the same game. The owl teaches you to tell them apart.",
              "es": "Jacquet, trictrac, backgammon: misma familia, mismo tablero… pero no el mismo juego. La lechuza os enseña a distinguirlos."},
  "body": body,
  "image": {"fr": "actu_fr.jpg", "en": "actu_en.jpg", "es": "actu_es.jpg"},
  "announce": {"active": True, "starts_at": None, "ends_at": "2027-03-13 23:59", "popup": True, "banner": True,
               "audience": "all", "color": "#c9954a", "emoji": "🦉", "newsletter": True,
               "title": {}, "text": {}, "btn": {"fr": "Voir la leçon", "en": "Watch the lesson", "es": "Ver la lección"},
               "image": {"fr": "actu_fr.jpg", "en": "actu_en.jpg", "es": "actu_es.jpg"}}
 }],
 "push": [{"ref": "lecon10-sortie", "send_at": "2027-02-28 18:00",
           "title": {"fr": "🦉 Leçon 10 : jacquet, trictrac et backgammon", "en": "🦉 Lesson 10: jacquet, trictrac and backgammon", "es": "🦉 Lección 10: jacquet, trictrac y backgammon"},
           "body": {"fr": "Même plateau, mais pas le même jeu : la chouette vous explique.", "en": "Same board, but not the same game: the owl explains.", "es": "Mismo tablero, pero no el mismo juego: la lechuza os lo explica."},
           "url": "/actu.php?a=lecon-10-jacquet-trictrac-backgammon"}],
 "metricool": []
}
bad = re.compile(r'\b(mise|pari|enjeu|à gagner|commission|rake|cagnotte|apuestas?|stake|money)\b', re.I)
txt = json.dumps(kit, ensure_ascii=False)
assert not bad.search(txt), bad.search(txt)
with zipfile.ZipFile('kit_lecon10.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('kit.json', json.dumps(kit, ensure_ascii=False, indent=1))
    for L, f in zip(('fr', 'en', 'es'), IMG):
        z.write(f, f'images/actu_{L}.jpg')
print('kit_lecon10.zip OK', YT)

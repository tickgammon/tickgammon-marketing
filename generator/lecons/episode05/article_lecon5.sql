-- 30/10/2026 — Article Actus : leçon 5 des Leçons de la chouette « Les probabilités aux dés » (sortie dim. 20/12/2026 à 10:30)
-- AVANT de l'importer : remplacer les 3 « ID_YOUTUBE » par l'identifiant de la vidéo YouTube.
-- À passer dans phpMyAdmin (base chouette), onglet SQL.
-- Publication PROGRAMMÉE : visible le dimanche 20/12/2026 à 10:30 (heure de Paris), invisible pour les joueurs avant.
-- Ensuite, dans l'admin 📰 Actus : ouvrir l'article, ajouter l'image miniature_lecon5_probabilites.jpg, garder la case
-- « 📣 Annoncer aussi sur le hub » cochée, enregistrer (garder la programmation au 20/12/2026 10:30).
-- Dans 📣 Annonces, mettre la fin de l'annonce au 02/01/2027 23:59 (veille de la leçon 6).
INSERT INTO news_articles (`slug`, `category`, `image`, `is_pinned`, `status`, `publish_at`,
  `title_fr`, `title_en`, `title_es`, `excerpt_fr`, `excerpt_en`, `excerpt_es`, `body_fr`, `body_en`, `body_es`)
SELECT 'lecon-5-probabilites', 'conseils', NULL, 0, 'published', '2026-12-20 10:30:00',
'Leçon 5 de la chouette : les probabilités aux dés',
'Owl lesson 5: dice probabilities',
'Lección 5 de la lechuza: las probabilidades de los dados',
'Au backgammon, la chance n''a rien de mystérieux. Dans sa nouvelle leçon vidéo, la chouette vous donne les quelques chiffres qui suffisent pour mieux jouer : 36 combinaisons, 11 chances sur 36, tirs directs et indirects.',
'In backgammon, luck is no mystery. In her new video lesson, the owl gives you the few numbers you need to play better: 36 combinations, 11 chances in 36, direct and indirect shots.',
'En el backgammon, la suerte no es ningún misterio. En su nueva lección en vídeo, la lechuza le da las pocas cifras que bastan para jugar mejor: 36 combinaciones, 11 posibilidades de 36, tiros directos e indirectos.',
'Ce qui fait peur à tous les débutants, c''est la chance. Pourtant, avec deux dés, tout se calcule ! Dans la leçon 5 des **Leçons de la chouette**, vous apprenez les chiffres clés des dés.

https://youtu.be/ID_YOUTUBE

## Au programme

- **Les 36 combinaisons** : pourquoi 6-1 et 1-6 comptent pour deux, et un double pour un seul.
- **Les lancers précis** : 2 chances sur 36 pour un lancer, 1 sur 36 pour un double précis, 6 sur 36 pour un double quelconque.
- **Au moins un chiffre** : 11 chances sur 36, soit environ 31 %, et un lancer vaut en moyenne un peu plus de 8 pips.
- **Le tir direct** : un blot à 6 cases ou moins est touché dans 31 à 47 % des cas.
- **Le tir indirect** : au-delà de 6 cases, le risque est divisé par deux, ou bien plus.
- **Rentrer depuis la barre** : vos chances selon le nombre de points ouverts.
- **Trois réflexes** : laisser le moins de tirs possible, éloigner ou cacher ses blots, regarder son jan intérieur avant de frapper.
- **Les dés et le videau** : la règle des 25 %, et pourquoi un coup malchanceux n''est pas un mauvais coup.

> Le conseil de la chouette : si vous devez laisser un blot, laissez-le plutôt à 7 cases ou plus !

## Pour aller plus loin

Retrouvez tous les chiffres dans notre [tableau des probabilités aux dés](/probabilites-des-backgammon.php). Et sur TickGammon, l''analyse de vos parties vous montre, coup par coup, si vous avez pris le bon risque.

La vidéo existe en français, en anglais et en espagnol : choisissez la langue dans ⚙️ → Piste audio. Prochaine leçon le **dimanche 3 janvier** : la chouette, le jeu à plusieurs.',
'What scares every beginner is luck. Yet with two dice, everything can be calculated! In lesson 5 of **The Owl''s Lessons**, you learn the key dice numbers.

https://youtu.be/ID_YOUTUBE

## In this lesson

- **The 36 combinations**: why 6-1 and 1-6 count as two, and a double as only one.
- **Specific rolls**: 2 chances in 36 for one roll, 1 in 36 for a specific double, 6 in 36 for any double.
- **At least one number**: 11 chances in 36, about 31%, and one roll is worth a little over 8 pips on average.
- **The direct shot**: a blot 6 points away or fewer gets hit 31 to 47% of the time.
- **The indirect shot**: beyond 6 points, the risk is cut in half, or even much more.
- **Coming in from the bar**: your chances depending on how many points are open.
- **Three reflexes**: leave as few shots as possible, move your blots away or hide them, check your home board before hitting.
- **Dice and the cube**: the 25% rule, and why an unlucky move isn''t a bad move.

> The owl''s tip: if you have to leave a blot, leave it 7 points away or more!

## Going further

Find all the numbers in our [dice probability tables](/probabilites-des-backgammon.php?lang=en). And on TickGammon, the analysis of your games shows you, move by move, whether you took the right risk.

The video is available in French, English and Spanish: choose the language in ⚙️ → Audio track. Next lesson on **Sunday 3 January**: the chouette, backgammon for several players.',
'Lo que asusta a todos los principiantes es la suerte. Sin embargo, ¡con dos dados todo se puede calcular! En la lección 5 de **Las lecciones de la lechuza**, aprenderá las cifras clave de los dados.

https://youtu.be/ID_YOUTUBE

## En esta lección

- **Las 36 combinaciones**: por qué 6-1 y 1-6 cuentan como dos, y un doble como uno solo.
- **Las tiradas concretas**: 2 posibilidades de 36 para una tirada, 1 de 36 para un doble concreto, 6 de 36 para cualquier doble.
- **Al menos un número**: 11 posibilidades de 36, más o menos un 31 %, y una tirada vale de media un poco más de 8 pips.
- **El tiro directo**: un blot a 6 casillas o menos es golpeado entre un 31 y un 47 % de las veces.
- **El tiro indirecto**: más allá de 6 casillas, el riesgo se divide por dos, o incluso mucho más.
- **Entrar desde la barra**: sus posibilidades según el número de puntos abiertos.
- **Tres reflejos**: dejar el menor número de tiros posible, alejar o esconder sus blots, mirar su cuadrante interior antes de golpear.
- **Los dados y el cubo**: la regla del 25 %, y por qué una jugada con mala suerte no es una mala jugada.

> El consejo de la lechuza: si tiene que dejar un blot, ¡déjelo mejor a 7 casillas o más!

## Para ir más lejos

Encuentre todas las cifras en nuestras [tablas de probabilidades de los dados](/probabilites-des-backgammon.php?lang=es). Y en TickGammon, el análisis de sus partidas le muestra, jugada a jugada, si ha corrido el riesgo adecuado.

El vídeo existe en francés, inglés y español: elija el idioma en ⚙️ → Pista de audio. Próxima lección el **domingo 3 de enero**: la chouette, el backgammon para varios jugadores.'
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM news_articles WHERE slug = 'lecon-5-probabilites');

-- Vérification : 1 ligne, status published, publish_at 2026-12-20 10:30:00
SELECT id, slug, status, publish_at, is_pinned FROM news_articles WHERE slug = 'lecon-5-probabilites';

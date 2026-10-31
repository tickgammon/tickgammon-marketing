-- 31/10/2026 — Article Actus : leçon 7 des Leçons de la chouette « Progresser contre l'ordinateur » (sortie dim. 17/1/2027 à 10:30)
-- AVANT de l'importer : remplacer les 3 « ID_YOUTUBE » par l'identifiant de la vidéo YouTube.
-- À passer dans phpMyAdmin (base chouette), onglet SQL.
-- Publication PROGRAMMÉE : visible le dimanche 17/01/2027 à 10:30 (heure de Paris), invisible pour les joueurs avant.
-- Ensuite, dans l'admin 📰 Actus : ouvrir l'article, ajouter les images par onglet : FR = miniature_lecon7_ordinateur.jpg,
-- EN = miniature_lecon7_ordinateur_en.jpg, ES = miniature_lecon7_ordinateur_es.jpg ; garder la case
-- « 📣 Annoncer aussi sur le hub » cochée, enregistrer (garder la programmation au 17/01/2027 10:30).
-- Dans 📣 Annonces, mettre la fin de l'annonce au 30/01/2027 23:59 (veille de la leçon 8).
INSERT INTO news_articles (`slug`, `category`, `image`, `is_pinned`, `status`, `publish_at`,
  `title_fr`, `title_en`, `title_es`, `excerpt_fr`, `excerpt_en`, `excerpt_es`, `body_fr`, `body_en`, `body_es`)
SELECT 'lecon-7-ordinateur', 'conseils', NULL, 0, 'published', '2027-01-17 10:30:00',
'Leçon 7 de la chouette : progresser contre l''ordinateur',
'Owl lesson 7: improving against the computer',
'Lección 7 de la lechuza: progresar contra el ordenador',
'Un adversaire qui ne dort jamais… et qui vous montre vos erreurs ! Dans sa nouvelle leçon vidéo, la chouette vous apprend à utiliser l''ordinateur pour progresser : GNU Backgammon, l''analyse de vos parties et une méthode en 3 étapes.',
'An opponent who never sleeps… and shows you your mistakes! In her new video lesson, the owl shows you how to use the computer to improve: GNU Backgammon, the analysis of your games and a 3-step method.',
'Un adversario que nunca duerme… ¡y que le muestra sus errores! En su nueva lección en vídeo, la lechuza le enseña a usar el ordenador para progresar: GNU Backgammon, el análisis de sus partidas y un método en 3 pasos.',
'Jouer contre un robot, ce n''est pas seulement pour s''occuper quand personne n''est là : bien utilisé, c''est le meilleur des professeurs. Dans la leçon 7 des **Leçons de la chouette**, vous apprenez à progresser contre l''ordinateur.

https://youtu.be/ID_YOUTUBE

## Au programme

- **Pourquoi l''ordinateur** : disponible à toute heure, sans pression, et un adversaire exigeant.
- **GNU Backgammon** : un logiciel libre et gratuit, basé sur des réseaux de neurones, plus fort que la grande majorité des joueurs.
- **Les dés sont honnêtes** : le robot n''a aucun avantage sur les dés, il place simplement ses pions là où beaucoup de lancers l''arrangent.
- **L''analyse** : le meilleur coup, votre coup, et combien chaque erreur vous a coûté.
- **Résultat ≠ jeu** : une victoire peut cacher des erreurs, une défaite peut venir des dés.
- **L''Entraînement** : des positions à travailler, et avec le Pack Sagesse, l''IA vous explique votre erreur en langage clair.
- **La méthode** : jouer une partie, la faire analyser, puis rejouer ses 2 ou 3 plus grosses erreurs.
- **Pour débuter** : perdre souvent au début est normal, chaque partie vous apprend quelque chose.

> Le conseil de la chouette : ne regardez pas seulement le résultat, l''analyse dit la vérité !

## Pour aller plus loin

Découvrez notre page [Jouer contre l''ordinateur](/backgammon-contre-ordinateur.php). Les parties contre les robots sont gratuites, dans votre navigateur, sur Android et sur Windows.

La vidéo existe en français, en anglais et en espagnol : choisissez la langue dans ⚙️ → Piste audio. Prochaine leçon le **dimanche 31 janvier** : jouer en ligne, le classement et l''ELO.',
'Playing against a bot isn''t just something to do when nobody''s around: used well, it''s the best teacher there is. In lesson 7 of **The Owl''s Lessons**, you learn how to improve against the computer.

https://youtu.be/ID_YOUTUBE

## In this lesson

- **Why the computer**: available at any time, no pressure, and a demanding opponent.
- **GNU Backgammon**: free and open-source software, based on neural networks, stronger than the vast majority of players.
- **Honest dice**: the bot has no advantage with the dice, it simply places its checkers where lots of rolls work for it.
- **The analysis**: the best move, your move, and how much each mistake cost you.
- **Result ≠ play**: a win can hide mistakes, a loss can come from the dice.
- **Training**: positions to work on, and with the Wisdom Pack, the AI explains your mistake in plain language.
- **The method**: play a game, have it analysed, then replay your 2 or 3 biggest mistakes.
- **Getting started**: losing often at first is normal, every game teaches you something.

> The owl''s tip: don''t just look at the result, the analysis tells the truth!

## Going further

Discover our page [Play against the computer](/backgammon-contre-ordinateur.php?lang=en). Games against the bots are free, in your browser, on Android and on Windows.

The video is available in French, English and Spanish: choose the language in ⚙️ → Audio track. Next lesson on **Sunday 31 January**: playing online, rankings and ELO.',
'Jugar contra un robot no es solo para pasar el rato cuando no hay nadie: bien usado, es el mejor de los profesores. En la lección 7 de **Las lecciones de la lechuza**, aprenderá a progresar contra el ordenador.

https://youtu.be/ID_YOUTUBE

## En esta lección

- **Por qué el ordenador**: disponible a cualquier hora, sin presión, y un adversario exigente.
- **GNU Backgammon**: un programa libre y gratuito, basado en redes neuronales, más fuerte que la gran mayoría de los jugadores.
- **Dados honestos**: el robot no tiene ninguna ventaja con los dados, simplemente coloca sus fichas donde muchas tiradas le vienen bien.
- **El análisis**: la mejor jugada, su jugada, y cuánto le ha costado cada error.
- **Resultado ≠ juego**: una victoria puede esconder errores, una derrota puede venir de los dados.
- **Entrenamiento**: posiciones para trabajar, y con el Pack Sabiduría, la IA le explica su error con palabras sencillas.
- **El método**: jugar una partida, hacer que se analice, y volver a jugar sus 2 o 3 errores más grandes.
- **Para empezar**: perder a menudo al principio es normal, cada partida le enseña algo.

> El consejo de la lechuza: no mire solo el resultado, ¡el análisis dice la verdad!

## Para ir más lejos

Descubra nuestra página [Jugar contra el ordenador](/backgammon-contre-ordinateur.php?lang=es). Las partidas contra los robots son gratuitas, en su navegador, en Android y en Windows.

El vídeo existe en francés, inglés y español: elija el idioma en ⚙️ → Pista de audio. Próxima lección el **domingo 31 de enero**: jugar en línea, la clasificación y el ELO.'
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM news_articles WHERE slug = 'lecon-7-ordinateur');

-- Vérification : 1 ligne, status published, publish_at 2027-01-17 10:30:00
SELECT id, slug, status, publish_at, is_pinned FROM news_articles WHERE slug = 'lecon-7-ordinateur';

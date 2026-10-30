-- 30/10/2026 — Article Actus : leçon 6 des Leçons de la chouette « La chouette, le jeu à plusieurs » (sortie dim. 3/1/2027 à 10:30)
-- AVANT de l'importer : remplacer les 3 « ID_YOUTUBE » par l'identifiant de la vidéo YouTube.
-- À passer dans phpMyAdmin (base chouette), onglet SQL.
-- Publication PROGRAMMÉE : visible le dimanche 03/01/2027 à 10:30 (heure de Paris), invisible pour les joueurs avant.
-- Ensuite, dans l'admin 📰 Actus : ouvrir l'article, ajouter les images par onglet : FR = miniature_lecon6_chouette.jpg,
-- EN = miniature_lecon6_chouette_en.jpg, ES = miniature_lecon6_chouette_es.jpg ; garder la case
-- « 📣 Annoncer aussi sur le hub » cochée, enregistrer (garder la programmation au 03/01/2027 10:30).
-- Dans 📣 Annonces, mettre la fin de l'annonce au 16/01/2027 23:59 (veille de la leçon 7).
INSERT INTO news_articles (`slug`, `category`, `image`, `is_pinned`, `status`, `publish_at`,
  `title_fr`, `title_en`, `title_es`, `excerpt_fr`, `excerpt_en`, `excerpt_es`, `body_fr`, `body_en`, `body_es`)
SELECT 'lecon-6-chouette', 'conseils', NULL, 0, 'published', '2027-01-03 10:30:00',
'Leçon 6 de la chouette : la chouette, le jeu à plusieurs',
'Owl lesson 6: the chouette, backgammon for a group',
'Lección 6 de la lechuza: la chouette, el juego en grupo',
'Le backgammon se joue à deux… sauf en chouette ! Dans sa nouvelle leçon vidéo, la chouette vous apprend à jouer à 3, 4, 5 joueurs ou plus autour d''un seul plateau : le box, le capitaine, l''équipe et un videau pour chacun.',
'Backgammon is a two-player game… except in a chouette! In her new video lesson, the owl shows you how to play with 3, 4, 5 or more players around a single board: the box, the captain, the team and a cube for everyone.',
'El backgammon se juega entre dos… ¡salvo en la chouette! En su nueva lección en vídeo, la lechuza le enseña a jugar entre 3, 4, 5 jugadores o más alrededor de un solo tablero: el box, el capitán, el equipo y un cubo para cada uno.',
'Une leçon qui tient particulièrement à cœur à notre chouette… puisque le jeu porte son nom ! Dans la leçon 6 des **Leçons de la chouette**, vous apprenez à jouer au backgammon à plusieurs.

https://youtu.be/ID_YOUTUBE

## Au programme

- **Le principe** : un joueur affronte seul toute une équipe, avec les règles habituelles du backgammon.
- **Les trois rôles** : le box joue contre tous, le capitaine lance les dés et déplace les pions, l''équipe le conseille.
- **Le tirage** : l''ordre des joueurs est tiré au sort ; le premier prend le box, le deuxième devient capitaine.
- **Les places tournent** : si le box gagne, il reste ; si le capitaine gagne, il prend le box.
- **Les points** : le box marque ou perd contre chaque joueur de l''équipe, par exemple 3 points d''un coup à quatre joueurs.
- **Un videau chacun** : chaque joueur de l''équipe accepte ou abandonne seul, et peut doubler le box avec son propre videau.
- **Pourquoi on aime la chouette** : on apprend vite, c''est convivial et c''est stratégique.
- **Conseils** : prudence dans le box, respect du capitaine, scores notés par écrit et règles fixées avant de commencer.

> Le conseil de la chouette : révisez le videau, c''est là que tout se joue en chouette !

## Pour aller plus loin

Retrouvez toutes les règles sur notre page [La chouette au backgammon](/chouette-backgammon.php). TickGammon est né de la chouette, et une chouette en ligne se prépare pour jouer à plusieurs, à distance.

La vidéo existe en français, en anglais et en espagnol : choisissez la langue dans ⚙️ → Piste audio. Prochaine leçon le **dimanche 17 janvier** : progresser contre l''ordinateur.',
'A lesson very close to our owl''s heart… since the game is named after her! In lesson 6 of **The Owl''s Lessons**, you learn how to play backgammon as a group.

https://youtu.be/ID_YOUTUBE

## In this lesson

- **The idea**: one player takes on a whole team alone, with the usual backgammon rules.
- **The three roles**: the box plays against everyone, the captain rolls the dice and moves the checkers, the team gives advice.
- **The draw**: the order of players is drawn at random; the first takes the box, the second becomes captain.
- **Rotating places**: if the box wins, they stay; if the captain wins, they take the box.
- **The points**: the box scores or loses against each team player, for example 3 points at once with four players.
- **A cube each**: each team player takes or passes alone, and can double the box with their own cube.
- **Why we love the chouette**: you learn fast, it''s social and it''s strategic.
- **Tips**: be careful in the box, respect the captain, keep the scores in writing and agree on the rules before you start.

> The owl''s tip: brush up on the doubling cube, that''s where everything happens in a chouette!

## Going further

Find all the rules on our page [The backgammon chouette](/chouette-backgammon.php?lang=en). TickGammon was born from the chouette, and an online chouette is on its way so you can play with several people remotely.

The video is available in French, English and Spanish: choose the language in ⚙️ → Audio track. Next lesson on **Sunday 17 January**: improving against the computer.',
'Una lección que nuestra lechuza aprecia especialmente… ¡porque el juego lleva su nombre! En la lección 6 de **Las lecciones de la lechuza**, aprenderá a jugar al backgammon en grupo.

https://youtu.be/ID_YOUTUBE

## En esta lección

- **La idea**: un jugador se enfrenta solo a todo un equipo, con las reglas habituales del backgammon.
- **Los tres papeles**: el box juega contra todos, el capitán tira los dados y mueve las fichas, el equipo le aconseja.
- **El sorteo**: el orden de los jugadores se sortea; el primero ocupa el box y el segundo es capitán.
- **Los puestos giran**: si gana el box, se queda; si gana el capitán, ocupa el box.
- **Los puntos**: el box gana o pierde puntos contra cada jugador del equipo, por ejemplo 3 puntos de golpe con cuatro jugadores.
- **Un cubo para cada uno**: cada jugador del equipo acepta o abandona por sí solo, y puede doblar al box con su propio cubo.
- **Por qué gusta la chouette**: se aprende rápido, es muy social y es estratégica.
- **Consejos**: prudencia en el box, respeto al capitán, resultados anotados por escrito y reglas fijadas antes de empezar.

> El consejo de la lechuza: repase el cubo doblador, ¡es ahí donde todo se decide en la chouette!

## Para ir más lejos

Encuentre todas las reglas en nuestra página [La chouette en backgammon](/chouette-backgammon.php?lang=es). TickGammon nació de la chouette, y estamos preparando una chouette en línea para jugar entre varios, a distancia.

El vídeo existe en francés, inglés y español: elija el idioma en ⚙️ → Pista de audio. Próxima lección el **domingo 17 de enero**: progresar contra el ordenador.'
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM news_articles WHERE slug = 'lecon-6-chouette');

-- Vérification : 1 ligne, status published, publish_at 2027-01-03 10:30:00
SELECT id, slug, status, publish_at, is_pinned FROM news_articles WHERE slug = 'lecon-6-chouette';

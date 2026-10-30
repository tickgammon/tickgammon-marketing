-- 30/10/2026 — Article Actus : leçon 4 des Leçons de la chouette « La course et la sortie des pions » (sortie dim. 6/12/2026 à 10:30)
-- AVANT de l'importer : remplacer les 3 « ID_YOUTUBE » par l'identifiant de la vidéo YouTube (ex. mhP6QNyFvfs).
-- À passer dans phpMyAdmin (base chouette), onglet SQL.
-- Publication PROGRAMMÉE : visible le dimanche 6/12/2026 à 10:30 (heure de Paris), invisible pour les joueurs avant.
-- Ensuite, dans l'admin 📰 Actus : ouvrir l'article, ajouter l'image miniature_lecon4_course.jpg, garder la case
-- « 📣 Annoncer aussi sur le hub » cochée, enregistrer (garder la programmation au 06/12/2026 10:30).
-- Dans 📣 Annonces, mettre la fin de l'annonce au 19/12/2026 23:59 (veille de la leçon 5).
INSERT INTO news_articles (`slug`, `category`, `image`, `is_pinned`, `status`, `publish_at`,
  `title_fr`, `title_en`, `title_es`, `excerpt_fr`, `excerpt_en`, `excerpt_es`, `body_fr`, `body_en`, `body_es`)
SELECT 'lecon-4-course', 'conseils', NULL, 0, 'published', '2026-12-06 10:30:00',
'Leçon 4 de la chouette : la course et la sortie des pions',
'Owl lesson 4: the race and bearing off',
'Lección 4 de la lechuza: la carrera y la salida de las fichas',
'C''est en fin de partie que beaucoup de matchs se jouent. Dans sa nouvelle leçon vidéo, la chouette vous apprend à compter les pips, à courir sans gaspiller et à sortir vos pions en toute sécurité.',
'Many matches are decided at the end of the game. In her new video lesson, the owl teaches you to count pips, race without wasting and bear off your checkers safely.',
'Muchas partidas se deciden al final. En su nueva lección en vídeo, la lechuza le enseña a contar los pips, a correr sin desperdiciar y a sacar sus fichas con total seguridad.',
'Vous connaissez les règles, les ouvertures et le videau : place à la fin de partie ! Dans la leçon 4 des **Leçons de la chouette**, vous apprenez à bien jouer la course et la sortie des pions.

https://youtu.be/ID_YOUTUBE

## Au programme

- **Qu''est-ce qu''une course** : le moment où plus aucun pion ne peut être frappé.
- **Compter les pips** : nombre de pions × numéro du point, et les 167 pips du départ.
- **Qui mène ?** Courir quand vous êtes devant, garder le contact quand vous êtes derrière.
- **Ramener ses pions** : penser en franchissements, jouer d''abord les pions les plus éloignés.
- **Ne pas gaspiller** : ne pas tout empiler sur le point 6.
- **La sortie sans contact** : sortir un pion à chaque fois, remplir les points vides.
- **La sortie avec contact** : la sécurité d''abord, vider les points depuis le plus éloigné.
- **Videau et gammon** : la règle des 8 % et 12 % en course, et comment éviter le gammon.

> Le conseil de la chouette : en course, une seule erreur coûte rarement la partie… mais dix petites erreurs, si !

## Pour aller plus loin

Retrouvez nos [10 conseils de stratégie pour débutants](/strategie-backgammon-debutant.php). Et sur TickGammon, l''analyse de vos parties vous indique le compte de pips à chaque coup.

La vidéo existe en français, en anglais et en espagnol : choisissez la langue dans ⚙️ → Piste audio. Prochaine leçon le **dimanche 20 décembre** : les probabilités aux dés.',
'You know the rules, the openings and the doubling cube: now for the end of the game! In lesson 4 of **The Owl''s Lessons**, you learn how to play the race and the bear-off well.

https://youtu.be/ID_YOUTUBE

## In this lesson

- **What is a race**: the moment when no checker can be hit anymore.
- **Counting pips**: number of checkers × point number, and the 167 pips at the start.
- **Who is ahead?** Run when you lead, keep contact when you trail.
- **Bringing checkers home**: think in crossovers, move your farthest checkers first.
- **Don''t waste pips**: don''t pile everything on the 6-point.
- **Bearing off with no contact**: bear off a checker every time, fill the empty points.
- **Bearing off with contact**: safety first, clear your points from the farthest one.
- **Cube and gammon**: the 8% and 12% rule in a race, and how to avoid a gammon.

> The owl''s tip: in a race, a single mistake rarely costs the game… but ten little mistakes do!

## Going further

Read our [10 strategy tips for beginners](/strategie-backgammon-debutant.php?lang=en). And on TickGammon, the analysis of your games shows you the pip count at every move.

The video is available in French, English and Spanish: choose the language in ⚙️ → Audio track. Next lesson on **Sunday 20 December**: dice probabilities.',
'Ya conoce las reglas, las aperturas y el cubo doblador: ¡llega el final de la partida! En la lección 4 de **Las lecciones de la lechuza**, aprenderá a jugar bien la carrera y la salida de las fichas.

https://youtu.be/ID_YOUTUBE

## En esta lección

- **Qué es una carrera**: el momento en que ya no se puede golpear ninguna ficha.
- **Contar los pips**: número de fichas × número del punto, y los 167 pips del inicio.
- **¿Quién va por delante?** Correr cuando va por delante, mantener el contacto cuando va por detrás.
- **Llevar las fichas a casa**: pensar en cruces, jugar primero las fichas más alejadas.
- **No desperdiciar**: no amontonarlo todo en el punto 6.
- **La salida sin contacto**: sacar una ficha cada vez, llenar los puntos vacíos.
- **La salida con contacto**: la seguridad primero, vaciar los puntos desde el más alejado.
- **Cubo y gammon**: la regla del 8 % y el 12 % en carrera, y cómo evitar el gammon.

> El consejo de la lechuza: en una carrera, un solo error rara vez cuesta la partida… ¡pero diez pequeños errores, sí!

## Para ir más lejos

Lea nuestros [10 consejos de estrategia para principiantes](/strategie-backgammon-debutant.php?lang=es). Y en TickGammon, el análisis de sus partidas le indica el recuento de pips en cada jugada.

El vídeo existe en francés, inglés y español: elija el idioma en ⚙️ → Pista de audio. Próxima lección el **domingo 20 de diciembre**: las probabilidades de los dados.'
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM news_articles WHERE slug = 'lecon-4-course');

-- Vérification : 1 ligne, status published, publish_at 2026-12-06 10:30:00
SELECT id, slug, status, publish_at, is_pinned FROM news_articles WHERE slug = 'lecon-4-course';

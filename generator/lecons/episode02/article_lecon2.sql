-- 30/10/2026 — Article Actus : leçon 2 des Leçons de la chouette « Les ouvertures » (sortie dim. 8/11/2026 à 10:30)
-- À passer dans phpMyAdmin (base chouette), onglet SQL.
-- Publication PROGRAMMÉE : visible le dimanche 8/11/2026 à 10:30 (heure de Paris), invisible pour les joueurs avant.
-- Ensuite, dans l'admin 📰 Actus : ouvrir l'article, ajouter l'image miniature_lecon2_ouvertures.jpg, enregistrer
-- (garder la programmation au 08/11/2026 10:30). Ne rien créer si l'article existe déjà.
-- La ligne seule https://youtu.be/mhP6QNyFvfs s'affiche comme lecteur vidéo (une seule vidéo, voix FR/EN/ES dans YouTube).
INSERT INTO news_articles (`slug`, `category`, `image`, `is_pinned`, `status`, `publish_at`,
  `title_fr`, `title_en`, `title_es`, `excerpt_fr`, `excerpt_en`, `excerpt_es`, `body_fr`, `body_en`, `body_es`)
SELECT 'lecon-2-ouvertures', 'conseils', NULL, 0, 'published', '2026-11-08 10:30:00',
'Leçon 2 de la chouette : les 15 ouvertures du backgammon',
'Owl lesson 2: the 15 backgammon openings',
'Lección 2 de la lechuza: las 15 aperturas del backgammon',
'Le premier coup de la partie n''a que 15 possibilités. Dans sa nouvelle leçon vidéo, la chouette vous apprend le meilleur coup pour chacune, en 6 minutes et demie.',
'The first move of the game has only 15 possibilities. In her new video lesson, the owl teaches you the best move for each one, in six and a half minutes.',
'La primera jugada de la partida solo tiene 15 posibilidades. En su nueva lección en vídeo, la lechuza le enseña la mejor jugada para cada una, en seis minutos y medio.',
'Après les règles, place à la pratique ! Dans la leçon 2 des **Leçons de la chouette**, vous apprenez à bien jouer le tout premier coup de la partie.

https://youtu.be/mhP6QNyFvfs

## Au programme

- **Pourquoi seulement 15 ouvertures** : le premier coup ne peut jamais être un double.
- **Lire un coup** : ce que veulent dire « 8/5 » ou « 13/11 (2) ».
- **Faire un point** avec 3-1, 4-2, 5-3, et le fameux **6-1** qui prend le bar point.
- **Courir avec un 6** : le « saut de l''amoureux » du 6-5, et les autres façons de sortir un pion arrière.
- **Préparer** avec des constructeurs pour tous les autres lancers.
- **Répondre avec un double**, du 6-6 au 1-1.
- **Les pièges à éviter** au deuxième coup.

> Le conseil de la chouette : ne cherchez pas à tout apprendre par cœur. Retenez d''abord les trois idées : faire un point, courir avec un 6, placer des constructeurs.

## Pour aller plus loin

Toutes les ouvertures sont réunies dans notre [tableau des ouvertures](/ouvertures-backgammon.php). Et sur TickGammon, l''analyse de vos parties vous montre quand vous vous écartez du meilleur coup, ouvertures comprises.

La vidéo existe en français, en anglais et en espagnol : choisissez la langue dans ⚙️ → Piste audio. Prochaine leçon le **dimanche 22 novembre** : bien utiliser le videau.',
'After the rules, it''s time to practise! In lesson 2 of **The Owl''s Lessons**, you learn how to play the very first move of the game well.

https://youtu.be/mhP6QNyFvfs

## In this lesson

- **Why only 15 openings**: the first move can never be a double.
- **Reading a move**: what "8/5" or "13/11 (2)" means.
- **Making a point** with 3-1, 4-2, 5-3, and the famous **6-1** that takes the bar point.
- **Running with a 6**: the "lover''s leap" with 6-5, and the other ways to bring out a back checker.
- **Building** with builders for all the other rolls.
- **Replying with a double**, from 6-6 to 1-1.
- **Traps to avoid** on the second move.

> The owl''s tip: don''t try to learn everything by heart. First remember the three ideas: make a point, run with a 6, place builders.

## Going further

All the openings are gathered in our [openings table](/ouvertures-backgammon.php?lang=en). And on TickGammon, the analysis of your games shows you when you stray from the best move, openings included.

The video is available in French, English and Spanish: choose the language in ⚙️ → Audio track. Next lesson on **Sunday 22 November**: using the doubling cube well.',
'Después de las reglas, ¡llega la práctica! En la lección 2 de **Las lecciones de la lechuza**, aprenderá a jugar bien la primerísima jugada de la partida.

https://youtu.be/mhP6QNyFvfs

## En esta lección

- **Por qué solo 15 aperturas**: la primera jugada nunca puede ser un doble.
- **Leer una jugada**: qué significan «8/5» o «13/11 (2)».
- **Hacer un punto** con 3-1, 4-2, 5-3, y el famoso **6-1** que se queda con el bar point.
- **Correr con un 6**: el «salto del enamorado» del 6-5, y las otras formas de sacar una ficha trasera.
- **Preparar** con constructores para todas las demás tiradas.
- **Responder con un doble**, del 6-6 al 1-1.
- **Las trampas que evitar** en la segunda jugada.

> El consejo de la lechuza: no intente aprenderlo todo de memoria. Recuerde primero las tres ideas: hacer un punto, correr con un 6, colocar constructores.

## Para ir más lejos

Todas las aperturas están reunidas en nuestra [tabla de aperturas](/ouvertures-backgammon.php?lang=es). Y en TickGammon, el análisis de sus partidas le muestra cuándo se aparta de la mejor jugada, aperturas incluidas.

El vídeo existe en francés, inglés y español: elija el idioma en ⚙️ → Pista de audio. Próxima lección el **domingo 22 de noviembre**: usar bien el cubo doblador.'
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM news_articles WHERE slug = 'lecon-2-ouvertures');

-- Vérification : 1 ligne, status published, publish_at 2026-11-08 10:30:00
SELECT id, slug, status, publish_at, is_pinned FROM news_articles WHERE slug = 'lecon-2-ouvertures';

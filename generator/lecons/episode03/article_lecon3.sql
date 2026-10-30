-- 30/10/2026 — Article Actus : leçon 3 des Leçons de la chouette « Bien utiliser le videau » (sortie dim. 22/11/2026 à 10:30)
-- ⚠️ AVANT DE LE PASSER : remplacer ID_YOUTUBE (3 fois) par l'identifiant de la vidéo YouTube (ex. mhP6QNyFvfs).
-- À passer dans phpMyAdmin (base chouette), onglet SQL.
-- Publication PROGRAMMÉE : visible le dimanche 22/11/2026 à 10:30 (heure de Paris), invisible pour les joueurs avant.
-- Ensuite, dans l'admin 📰 Actus : ouvrir l'article, ajouter l'image miniature_lecon3_videau.jpg, laisser cochée
-- « 📣 Annoncer aussi sur le hub », enregistrer (garder la programmation au 22/11/2026 10:30).
-- Puis dans 📣 Annonces : fin de l'annonce au 05/12/2026 23:59 (veille de la leçon 4). Ne rien créer si l'article existe déjà.
INSERT INTO news_articles (`slug`, `category`, `image`, `is_pinned`, `status`, `publish_at`,
  `title_fr`, `title_en`, `title_es`, `excerpt_fr`, `excerpt_en`, `excerpt_es`, `body_fr`, `body_en`, `body_es`)
SELECT 'lecon-3-videau', 'conseils', NULL, 0, 'published', '2026-11-22 10:30:00',
'Leçon 3 de la chouette : bien utiliser le videau',
'Owl lesson 3: using the doubling cube well',
'Lección 3 de la lechuza: usar bien el cubo doblador',
'Quand doubler, quand accepter ? Dans sa nouvelle leçon vidéo, la chouette vous explique le videau et la fameuse règle des 25 %, en 6 minutes et demie.',
'When to double, when to take? In her new video lesson, the owl explains the doubling cube and the famous 25% rule, in six and a half minutes.',
'¿Cuándo doblar, cuándo aceptar? En su nueva lección en vídeo, la lechuza le explica el cubo doblador y la famosa regla del 25 %, en seis minutos y medio.',
'Savoir quand doubler et quand accepter compte autant que bien déplacer ses pions. Dans la leçon 3 des **Leçons de la chouette**, le videau n''aura plus de secret pour vous.

https://youtu.be/ID_YOUTUBE

## Au programme

- **Le videau, c''est quoi** : ce gros dé marqué 2, 4, 8, 16, 32 et 64.
- **Comment ça marche** : proposer de doubler, accepter ou refuser, et qui garde le videau.
- **Le videau multiplie tout** : un gammon avec le videau à 4 vaut 8 points.
- **La règle des 25 %** : le calcul le plus important du backgammon.
- **Quand doubler** : ni trop tôt, ni trop tard.
- **Les situations typiques** : la course, l''attaque, le blocage… et « trop bien pour doubler ».
- **Les règles spéciales** : Crawford, Jacoby et le beaver.
- **Les 3 erreurs** les plus fréquentes des débutants.

> Le conseil de la chouette : si vous gagnez au moins une partie sur quatre dans cette position, acceptez le double !

## Pour aller plus loin

Retrouvez la règle des 25 % et tous ces conseils sur notre [page du videau](/videau-backgammon.php). Et sur TickGammon, l''analyse de vos parties vous montre chaque décision de videau discutable.

La vidéo existe en français, en anglais et en espagnol : choisissez la langue dans ⚙️ → Piste audio. Prochaine leçon le **dimanche 6 décembre** : la course et la sortie des pions.',
'Knowing when to double and when to take matters just as much as moving your checkers well. In lesson 3 of **The Owl''s Lessons**, the doubling cube will hold no more secrets for you.

https://youtu.be/ID_YOUTUBE

## In this lesson

- **What the doubling cube is**: that big die marked 2, 4, 8, 16, 32 and 64.
- **How it works**: offering a double, taking or passing, and who keeps the cube.
- **The cube multiplies everything**: a gammon with the cube on 4 is worth 8 points.
- **The 25% rule**: the most important calculation in backgammon.
- **When to double**: neither too early nor too late.
- **Typical situations**: the race, the attack, the blockade… and "too good to double".
- **Special rules**: Crawford, Jacoby and the beaver.
- **The 3 most common** beginner mistakes.

> The owl''s tip: if you win at least one game in four from this position, take the double!

## Going further

Find the 25% rule and all these tips on our [doubling cube page](/videau-backgammon.php?lang=en). And on TickGammon, the analysis of your games shows you every questionable cube decision.

The video is available in French, English and Spanish: choose the language in ⚙️ → Audio track. Next lesson on **Sunday 6 December**: the race and bearing off.',
'Saber cuándo doblar y cuándo aceptar cuenta tanto como mover bien las fichas. En la lección 3 de **Las lecciones de la lechuza**, el cubo doblador ya no tendrá secretos para usted.

https://youtu.be/ID_YOUTUBE

## En esta lección

- **Qué es el cubo doblador**: ese dado grande marcado con 2, 4, 8, 16, 32 y 64.
- **Cómo funciona**: proponer doblar, aceptar o rechazar, y quién se queda con el cubo.
- **El cubo lo multiplica todo**: un gammon con el cubo en 4 vale 8 puntos.
- **La regla del 25 %**: el cálculo más importante del backgammon.
- **Cuándo doblar**: ni demasiado pronto ni demasiado tarde.
- **Situaciones típicas**: la carrera, el ataque, el bloqueo… y «demasiado bien para doblar».
- **Reglas especiales**: Crawford, Jacoby y el beaver.
- **Los 3 errores** más frecuentes de los principiantes.

> El consejo de la lechuza: si gana al menos una partida de cada cuatro en esa posición, ¡acepte el doble!

## Para ir más lejos

Encuentre la regla del 25 % y todos estos consejos en nuestra [página del cubo doblador](/videau-backgammon.php?lang=es). Y en TickGammon, el análisis de sus partidas le muestra cada decisión de cubo discutible.

El vídeo existe en francés, inglés y español: elija el idioma en ⚙️ → Pista de audio. Próxima lección el **domingo 6 de diciembre**: la carrera y la salida de las fichas.'
FROM DUAL
WHERE NOT EXISTS (SELECT 1 FROM news_articles WHERE slug = 'lecon-3-videau');

-- Vérification : 1 ligne, status published, publish_at 2026-11-22 10:30:00
SELECT id, slug, status, publish_at, is_pinned FROM news_articles WHERE slug = 'lecon-3-videau';

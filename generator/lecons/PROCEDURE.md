# 🦉 Procédure complète — une leçon vidéo de la chouette (validée sur la leçon 2, 30/10/2026)

Une leçon = **1 seule vidéo YouTube pour FR/EN/ES** (voix FR dans la vidéo, voix EN et ES en pistes audio YouTube),
24 Shorts, 3 miniatures, 3 sous-titres, 1 article Actus + annonce du hub, la vidéo sur la page du site.
Sortie : **dimanche 10:30** (heure de Paris), une leçon tous les 2 dimanches. Dossier modèle : `generator/lecons/episode02/`.

---

## ÉTAPE 1 — Le script (Claude, le mercredi avant la sortie, ou en avance)

1. Lire la page du site de la leçon (`tickgammon-site`, après `git pull`) : c'est la source du contenu.
2. Écrire `episodeNN/passages_fr.txt`, `passages_en.txt`, `passages_es.txt`, format `Pxx|chapitre|texte` :
   - chapitre **0** = introduction, **1 à 8** = les 8 chapitres, **9** = conclusion ;
   - FR ≈ 1 000 à 1 100 mots, **vouvoiement** ; EN ; ES au **« vosotros »** (comme les leçons 1 à 3) ;
   - **un seul `[laughs]`** ; la fin annonce la leçon suivante + « Abonnez-vous » + « jouez gratuitement… navigateur, Android, Windows » ;
   - **jamais** : mise, pari, enjeu, à gagner, commission, rake, cagnotte, apuestas, money, stake (dire « valeur de la partie ») ;
   - les coups sont écrits en toutes lettres (« de huit à cinq »).
3. `python3 mkblocs.py` (copier celui de l'épisode précédent, changer le n° d'épisode et les bornes) → `blocs_episodeN_FR/EN/ES.txt`.
   **Règle obligatoire des 3 blocs : bloc 1 = chapitres 0 à 3, bloc 2 = chapitres 4 à 6, bloc 3 = chapitres 7 à 9**
   (c'est ce qu'attend `align.py`). Chaque bloc < 2 500 caractères.
4. Commit + push, puis **envoyer les 3 fichiers blocs à Joyce** et lui demander de relire le FR.

## ÉTAPE 2 — L'audio (Joyce, au plus tard le jeudi)

ElevenLabs, voix **MIMI**, modèle **Eleven v4**, mêmes réglages. 9 fichiers :
`bloc1.mp3 bloc2.mp3 bloc3.mp3 bloc1_en.mp3 bloc2_en.mp3 bloc3_en.mp3 bloc1_es.mp3 bloc2_es.mp3 bloc3_es.mp3`.

## ÉTAPE 3 — La fabrication (Claude)

Travailler dans le scratchpad (`…/scratchpad/epN/`), y copier : les 9 MP3, `passages_*.txt`, `align.py`, et depuis
`episode02/` : `cut_multi.py`, `render2.js`, `ev2.js`, `srt2.py`, `short_bg2.js`, `shorts2.py`, `thumb2.js`, plus
`audio_lecon.py`, `short_bg.html`, `*.woff2`, `owl_base.png`, `owl_wing.png`, `logo_circle.png` du dossier parent.

1. **Alignement** : `python3 align.py fr` / `en` / `es`. Contrôler le tableau durée réelle / attendue de chaque passage
   (écart > 30 % = problème de découpage → vérifier avant d'aller plus loin).
2. **Minutage commun** : `python3 cut_multi.py` → chaque passage dure le max des 3 langues ; produit `voice_fr/en/es.wav`,
   `timeline.json` (commun) et `timeline_fr/en/es.json` (pour les sous-titres).
3. **Les animations** : écrire `leconN.html` (partir de `lecon2.html` : même moteur plateau/chouette, nouvelles scènes `SC.P01…`).
   Règles de l'image commune aux 3 langues :
   - sur le plateau : **chiffres et symboles seulement** (dés, « 8/5 », cadenas, flèches, ✓ ✗) ; mots du jeu acceptés : BLOT, PRIME, BAR POINT ;
   - titres de chapitre : **FR en grand + EN et ES en dessous** (tableau `CH`) ; **pas de sous-titres incrustés** ;
   - carte « coup » en haut à droite (`X.note`) ; chouette en bas à droite ;
   - **dernière scène (20 dernières secondes) : laisser VIDES le coin bas-gauche (élément vidéo YouTube) et le coin
     bas-droit (bouton S'abonner)** — les éléments de l'écran de fin YouTube ne se réduisent pas ;
   - écran titre et fin : `tickgammon.com`, « Web · Android · Windows », carte de la leçon suivante.
4. **Contrôle visuel AVANT le rendu complet** : `node render2.js fr 0 0 test <temps à 75 % de chaque passage>` puis
   planches de 6 images ; corriger jusqu'à ce que tout soit juste.
5. **Rendu** : N = total × 30 ; lancer 6 morceaux `node render2.js fr a b frames` en parallèle (≈ 35 min).
   **Vérifier qu'il ne manque aucune image** (f00000 → fN-1) avant d'encoder. Surveiller le disque.
6. **Bruitages** : `node ev2.js` puis le petit script Python (pops des pions, clics des dés, whoosh entre chapitres,
   tada intro/fin, chime fin) → `ev.json` ; `python3 audio_lecon.py TOTAL ev.json bed.wav`.
7. **Mix par langue** (musique **0.22**, compresseur sur la voix, −14 LUFS) :
   ```
   ffmpeg -i bed.wav -i voice_L.wav -filter_complex "[1]aresample=44100,aformat=channel_layouts=stereo,apad[v];[v]asplit[v1][v2];[0]volume=0.22[m];[m][v1]sidechaincompress=threshold=0.04:ratio=5:attack=20:release=450[md];[md][v2]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000" -t TOTAL mix_L.wav
   ```
   Contrôle : musique seule ≈ −26 dB, passage parlé ≈ −17 dB (comme la leçon 1).
8. **Vidéo** (voix FR) : `ffmpeg -framerate 30 -i frames/f%05d.jpg -i mix_fr.wav -c:v libx264 -preset slow -pix_fmt yuv420p -b:v 8M -minrate 6M -maxrate 10M -bufsize 16M -x264-params nal-hrd=vbr -c:a aac -b:a 192k -shortest -movflags +faststart leconN_<sujet>_16x9.mp4`
   → `ffprobe` (1920×1080, durée), **puis supprimer le dossier `frames/`**.
9. **Pistes audio YouTube** : `mix_en.wav` et `mix_es.wav` → MP3 320k `leconN_<sujet>_piste_en.mp3` / `_es.mp3`.
10. **Sous-titres** : `python3 srt2.py fr|en|es leconN_<sujet>_xx.srt`.
11. **Shorts** : adapter `short_bg2.js` (épisode + 8 titres de chapitre FR/EN/ES) → `node short_bg2.js` ;
    `python3 shorts2.py fr|en|es` (vidéo + mix de la langue) → 24 Shorts 1080×1920.
12. **Miniatures** : adapter les textes de `thumb2.js` (« Leçon N », titre, accroche, scène choisie) → `node thumb2.js fr|en|es`.
13. **GitHub** (`tickgammon-marketing`) : générateur dans `generator/lecons/episodeNN/`, Shorts + .srt + pistes MP3 dans
    `videos/lecons/episodeNN/`, miniatures dans `visuels/lecons/`. **La vidéo complète (≈ 400 Mo) ne va pas sur GitHub.**

## ÉTAPE 4 — Ce que Claude envoie à Joyce (un fichier par envoi pour les gros fichiers)

1. la vidéo `leconN_<sujet>_16x9.mp4` ;
2. `…_piste_en.mp3` (envoi séparé) ; 3. `…_piste_es.mp3` (envoi séparé) ;
4. les 3 `.srt` ; 5. les 3 miniatures FR/EN/ES ;
6. le **titre + la description FR/EN/ES** avec les chapitres (temps = début de chaque chapitre − 1,8 s) et la ligne
   « 🤖 Voix et animations créées avec l'aide de l'IA. » / « 🤖 Voice and animations created with the help of AI. » /
   « 🤖 Voz y animaciones creadas con ayuda de la IA. » ;
7. les **tags** ; 8. `lecons_lib.php` ; 9. `article_leconN.sql` + l'image de couverture (= miniature FR) ;
10. la marche à suivre YouTube ci-dessous.

## ÉTAPE 5 — YouTube Studio (Joyce)

1. **Créer → Importer des vidéos** → la vidéo.
2. **Détails** : titre FR, description FR, **miniature FR**, playlist **« Les leçons de la chouette — apprendre le backgammon »**,
   « Non, elle n'est pas conçue pour les enfants ».
3. **Afficher plus** : Promotion rémunérée **Non** ; Utilisation de l'IA **Oui** ; Chapitres automatiques décochés ; Tags ;
   **Langue de la vidéo : Français** (vérifier, YouTube met parfois Anglais) ; Catégorie **Éducation** ;
   Sous-titres → Importer un fichier → **« Avec les données de synchronisation »** → `…_fr.srt`.
4. **Éléments de la vidéo → Écran de fin** : modèle « 1 vidéo, 1 élément S'abonner » ; vidéo = « Contenu adapté au
   spectateur » (le choix Playlist n'est pas dans cet élément) ; les 2 éléments sur les **20 dernières secondes** ;
   vidéo en bas à gauche, S'abonner en bas à droite. ⚠️ L'écran de fin **ne s'affiche pas tant que la vidéo est privée/programmée** : c'est normal.
5. **Visibilité → Programmer** : dimanche **10:30**.
6. Menu **Langues** → la vidéo → **Ajouter une langue** : Anglais puis Espagnol ; pour chacune :
   Sous-titres (fichier .srt, avec synchronisation), **Doublage** (le MP3 de la langue), Titre et description,
   Miniature si YouTube la propose. (Doublage = « fonctionnalités avancées » : vérification par téléphone si demandé.)
7. Normal juste après l'envoi : « Une erreur s'est produite » pendant le traitement ; qualité 240p au début
   (le 1080p arrive après le traitement HD ; YouTube ne permet pas d'imposer la qualité).

## ÉTAPE 6 — Les 24 Shorts dans Metricool (Claude, blogId 7411766, Europe/Paris)

- 8 jours entre le lendemain de la sortie et la veille de la leçon suivante, **sans tomber les jours des Shorts de la
  leçon précédente** (vérifier avec getScheduledPosts).
- **FR 12:30** : twitter, facebook (REEL), tiktok, youtube (short), bluesky. **EN 16:00** et **ES 20:00** : tiktok + youtube.
- Média : `https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/main/videos/lecons/episodeNN/shorts/leconN_L_chapC_9x16.mp4`
- Texte FR : `🦉 Les leçons de la chouette · Leçon N, chapitre C : <titre>\n<accroche>\nLeçon complète sur YouTube · jouez gratuitement 👉 https://www.tickgammon.com\n#backgammon #jeudesociete`
  (EN : The Owl's Lessons · Lesson N, chapter C … #backgammon #boardgames ; ES : Las lecciones de la lechuza · Lección N, capítulo C … #backgammon #juegosdemesa).
- youtubeData : titre `<titre> 🦉 <nom de la leçon> #shorts`, type short, public, tags, EDUCATION, madeForKids false,
  **isAiGeneratedContent true** ; tiktokData : PUBLIC_TO_EVERYONE, commercialContentOwnBrand true, title, **isAigc true** ;
  facebookData : REEL + titre « <titre> — Les leçons de la chouette » ; blueskyData : postLanguages fr ; texte alternatif FR.

## ÉTAPE 7 — Le site (Claude prépare, Joyce met en ligne)

1. **`lecons_lib.php`** : dans la ligne de la leçon, `'yt' => ['fr' => '<ID YouTube>', 'en' => '', 'es' => '']`
   (EN/ES vides = même vidéo). À mettre en ligne dès que l'ID est connu : la page garde le teaser jusqu'au dimanche 10:30
   puis affiche la vidéo toute seule. Livrer le fichier complet + `php -l`.
2. **Article Actus** `article_leconN.sql` (modèle : `article_lecon2.sql`) : slug `lecon-N-<sujet>`, catégorie `conseils`,
   `status 'published'`, `publish_at` = dimanche **10:30**, titres + chapôs + textes FR/EN/ES, le lien `https://youtu.be/<ID>`
   **seul sur sa ligne** (= lecteur vidéo), programme de la leçon, conseil de la chouette, lien vers la page (`?lang=en/es`),
   phrase « choisissez la langue dans ⚙️ → Piste audio », date de la leçon suivante. Joyce : phpMyAdmin → SQL, puis 📰 Actus →
   image = miniature FR, **case « 📣 Annoncer aussi sur le hub » cochée** → enregistrer.
3. **Annonce du hub** : créée par cette case (du dimanche 10:30, 14 jours). Mettre la fin à la **veille de la leçon
   suivante 23:59**. « (sans titre) » et « ⚠️ Article indisponible » avant la sortie = **normal** (l'article est programmé).
   Secours si la case n'a rien créé : `annonce_leconN.sql` (modèle : `annonce_lecon2.sql`).

## ÉTAPE 8 — Rappels et vérification

- Document **Rappels** + **Google Agenda** (`tickgammon@gmail.com`, Europe/Paris) : « Avant le dimanche : `lecons_lib.php`,
  article, annonce » et **dimanche 10:35** : vérifier sur `https://youtu.be/<ID>` l'écran de fin (à −20 s, ordinateur +
  téléphone), ⚙️ → Piste audio EN/ES, sous-titres, ⚙️ → Qualité 1080p, la vidéo sur la page du site, l'annonce sur le hub.
- Cocher les étapes faites dans Rappels.

# TickGammon — vidéos marketing

Dépôt **public** qui contient uniquement les vidéos promotionnelles de TickGammon et le générateur qui les fabrique.
Aucun code du site tickgammon.com ici. Les vidéos sont servies publiquement (liens `raw.githubusercontent.com`)
pour que Metricool puisse les publier automatiquement.

## Campagne SEO « 1 sujet par semaine »

12 sujets = les 12 pages publiques du site (règles, ouvertures, videau…). Chaque semaine :

| Jour | Langue | Réseaux automatiques (Metricool) |
|---|---|---|
| Lundi 18 h 30 | Français | TikTok, YouTube Shorts, Bluesky |
| Mercredi 18 h 30 | Anglais | TikTok, YouTube Shorts, Bluesky |
| Vendredi 12 h | Espagnol | TikTok, YouTube Shorts, Bluesky |

Calendrier complet : `generator/calendar.json` (pause du 21/12/2026 au 03/01/2027).

## Organisation

```
generator/
  subjects.json   contenu des 12 vidéos (FR / EN / ES) — tiré des pages du site
  calendar.json   semaine → sujet → dates de publication
  template.html   la vidéo (scènes, animations, 4 formats)
  render.js       capture des images (Playwright / Chromium)
  audio.py        musique pop originale + bruitages (aucun droit d'auteur)
  logo.js, owl_base.png, owl_wing.png   la chouette officielle (coucou + clin d'œil)
  build.sh        fabrique les 12 vidéos d'un sujet
videos/<NN>_<sujet>/<sujet>_<langue>_<format>.mp4
```

Formats : `vertical` (9:16, TikTok / Shorts / Reels / Stories), `portrait` (4:5, fil Instagram / Facebook),
`carre` (1:1, Bluesky / WhatsApp / LinkedIn), `paysage` (16:9, X / Discord).

## Fabriquer un sujet

```bash
bash generator/build.sh regles
```

Prérequis : Node + Playwright (Chromium dans `/opt/pw-browsers/chromium`), Python 3 + numpy + scipy, ffmpeg.

## Règles de contenu

- La chouette du logo, jamais redessinée.
- Aucun mot lié aux paris, mises ou gains (règles TikTok).
- La chouette (jeu à plusieurs) est annoncée « bientôt en ligne ».
- Pas d'iPhone dans les plateformes tant que l'appli App Store n'est pas publiée.

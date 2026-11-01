# Visuel « Résultats » d'un tournoi officiel (01/11/2026)

Utilisé par la tâche planifiée « Résultats des tournois officiels » (chaque jour vers 8:45, posts à 9:00).

1. Lire les tournois terminés : https://www.tickgammon.com/event_results.php?hours=24 (JSON : nom, podium, TGC).
2. Écrire un JSON : `{"id":N,"name":"…","theme":"felt|halloween|noel","total":TGC,"podium":[{"name":"…","tgc":600},…]}`
   - theme : `halloween` en octobre (fin de mois), `noel` en décembre, sinon `felt` (vert TickGammon).
   - total : somme des TGC gagnés (champ `total_tgc`).
3. `node generator/resultats/resultat.js fichier.json` → `visuels/resultats/resultats-<id>-<fr|en|es>.png` et `.jpg`.
4. Push sur main. Liens : https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/main/visuels/resultats/resultats-<id>-<langue>.<png|jpg>
   - **TikTok n'accepte que le .jpg** (pas le PNG).

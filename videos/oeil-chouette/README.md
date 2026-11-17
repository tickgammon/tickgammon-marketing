# 👁️ Lancement « L'œil de la chouette » (mar. 1/12/2026)

Kit fabriqué le 17/11/2026. Les posts Metricool sont en **brouillon**, à valider par Joyce.

| Fichier | Durée | Usage |
|---|---|---|
| `tease1_oeil_<fr|en|es>_vertical.mp4` | 10 s | Teaser du mar. 24/11 : « La chouette ouvre l'œil… », plateau flou |
| `tease2_oeil_<fr|en|es>_vertical.mp4` | 10 s | Teaser du jeu. 26/11 : « Un plateau, une photo… » |
| `launch_oeil_<fr|en|es>_vertical.mp4` | 26 s | Lancement du 1/12 : photo, lecture, meilleur coup expliqué, offres, bouton 📷 SCAN |
| `couverture_oeil_<fr|en|es>.jpg` | — | Couverture de l'Actu (1600 × 900), incluse dans kit_oeil_chouette.zip |
| `TEXTES.md` | — | Annonce de la Friday Cup du 27/11, WhatsApp, push, planning Metricool, défi #TickScan (à valider) |

Refabriquer : `bash generator/oeil/build.sh [tease1 tease2 launch cover]`. Posts : `python3 generator/oeil/mk_metricool.py <commit> <sortie.json>`.

Règles :
- aucune mention IA à l'écran : la déclaration passe par les cases Metricool ;
- aucun mot de jeu d'argent ;
- la chouette officielle seulement ;
- pas d'iPhone : le site, Android et Windows.

# Friday Cup — visuel « Champion de la semaine »

Visuel carré 1080×1080 (style du canvas Friday Cup : feutre vert, chouette au trophée, ticket crème), en FR, EN et ES.

```
node generator/fridaycup/champion.js <édition> "<vainqueur>" "<finaliste>"
# ex. node generator/fridaycup/champion.js 1 "GuyLabesse" "Marie64"
```

Sortie : `visuels/friday-cup/champion-<NN>-fr.png`, `-en.png`, `-es.png`. Après `git push`, lien public pour Metricool :
`https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/main/visuels/friday-cup/champion-<NN>-<langue>.png`

- Les polices sont dans `fonts/` (Google Fonts n'est pas joignable depuis l'espace de travail).
- Un pseudo long est réduit automatiquement pour tenir dans sa colonne.
- Textes publics : pas de vocabulaire de paris (« TGC offerts », jamais « à gagner »).

#!/bin/bash
# Fabrique les vidéos « 👁️ L'œil de la chouette » dans videos/oeil-chouette/ (17/11/2026)
#   tease1 : teaser mystère du mar. 24/11 (10 s) · tease2 : teaser du jeu. 26/11 (10 s) · launch : lancement du 1/12 (26 s)
#   cover  : couvertures de l'Actu FR/EN/ES (1600 × 900, dans le kit)
# Usage : bash generator/oeil/build.sh [tease1 tease2 launch cover]
set -e
cd "$(dirname "$0")"
OUT="../../videos/oeil-chouette"; TMP="/tmp/tgm_oe"; mkdir -p "$OUT" "$TMP"
VIDS="${@:-tease1 tease2 launch cover}"
for V in $VIDS; do
  if [ "$V" = cover ]; then
    for L in fr en es; do node render.js cover $L cover "$TMP/c_$L" 0.5 >/dev/null
      python3 -c "from PIL import Image;Image.open('$TMP/c_$L/f0000.jpg').convert('RGB').resize((1600,900),Image.LANCZOS).save('$OUT/couverture_oeil_$L.jpg',quality=88)"; done; continue; fi
  case $V in
    tease1) DUR=10; SEED=8;; tease2) DUR=10; SEED=9;; launch) DUR=26; SEED=5;;
  esac
  python3 - "$V" > "$TMP/ev_$V.json" <<'PY'
import json,sys
v=sys.argv[1]
ev={'pop':[],'click':[],'ting':[],'whoosh':[],'tada':[],'chime':[]}
def cuts(ts):
    for t in ts: ev['whoosh'].append(t-0.2); ev['pop']+=[[t+0.1,900],[t+0.35,1200]]
if v in('tease1','tease2'):
    ev['pop']+=[[0.15,700],[0.4,1000]]; ev['ting']+=[1.2,2.6]
    if v=='tease2': ev['click']+=[1.85,1.9]
    ev['whoosh'].append(5.2); ev['tada'].append(5.5); ev['chime'].append(8.8)
if v=='launch':
    ev['pop']+=[[0.4,700],[0.6,1000],[0.9,1100]]; ev['ting']+=[1.7]
    cuts([3.6,8.2,12.6,17.0]); ev['click']+=[3.6+1.85,3.6+1.9]
    ev['ting']+=[8.2+3.0]; ev['pop']+=[[12.6+0.5+i*0.35,1000+i*80] for i in range(3)]
    ev['pop']+=[[17.0+0.5+i*0.4,900+i*120] for i in range(4)]
    ev['whoosh'].append(21.2); ev['tada'].append(21.45); ev['ting']+=[22.7]; ev['chime'].append(24.6)
print(json.dumps(ev))
PY
  python3 ../audio.py "$DUR" "$TMP/ev_$V.json" "$TMP/audio_$V.wav" "$SEED"
  for L in fr en es; do node render.js "$V" "$L" vertical "$TMP/f_${V}_${L}" & done; wait
  for L in fr en es; do
    ffmpeg -loglevel error -y -framerate 30 -i "$TMP/f_${V}_${L}/f%04d.jpg" -i "$TMP/audio_$V.wav" \
      -vf "scale=1080:1920:flags=lanczos,format=yuv420p" -c:v libx264 -preset medium -crf 22 \
      -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:a aac -b:a 160k -ar 44100 -shortest -movflags +faststart \
      "$OUT/${V}_oeil_${L}_vertical.mp4"
    rm -rf "$TMP/f_${V}_${L}"
  done
done
ls -la "$OUT"

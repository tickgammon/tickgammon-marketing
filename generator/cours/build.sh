#!/bin/bash
# Fabrique la campagne « Cours TickGammon » dans videos/cours/
#   collectifs, particuliers, prof : vertical + carré ; whatsapp : carré + vertical (FR/EN/ES)
# Usage : bash generator/cours/build.sh [collectifs particuliers prof whatsapp]
set -e
cd "$(dirname "$0")"
OUT="../../videos/cours"; TMP="/tmp/tgm_cours"; mkdir -p "$OUT" "$TMP"
VIDS="${@:-collectifs particuliers prof whatsapp}"
for V in $VIDS; do
  case $V in
    collectifs) SEED=4; NAME=cours_collectifs;;
    particuliers) SEED=6; NAME=cours_particuliers;;
    prof) SEED=9; NAME=devenir_prof;;
    whatsapp) SEED=2; NAME=cours_whatsapp;;
  esac
  for L in fr en es; do
    for F in vertical carre; do node render.js "$V" "$L" "$F" "$TMP/f_${V}_${L}_${F}" & done; wait
    if [ ! -f "$TMP/audio_$V.wav" ]; then
      python3 - "$TMP/f_${V}_${L}_vertical/cuts.json" > "$TMP/ev_$V.json" <<'PY'
import json,sys
c=json.load(open(sys.argv[1]));cuts=c['CUTS'];end=c['END']
ev={'pop':[[0.4,700],[0.6,1000],[0.9,1100]],'click':[],'ting':[1.7],'whoosh':[],'tada':[],'chime':[]}
for t in cuts[1:-1]:
    ev['whoosh'].append(t-0.2); ev['pop']+=[[t+0.1,900],[t+0.35,1200]]
o=cuts[-1]; ev['whoosh'].append(o-0.2); ev['tada'].append(o+0.05); ev['ting'].append(o+1.3); ev['chime'].append(end-1.2)
print(json.dumps(ev))
PY
      DUR=$(python3 -c "import json;print(json.load(open('$TMP/f_${V}_${L}_vertical/cuts.json'))['END'])")
      python3 ../audio.py "$DUR" "$TMP/ev_$V.json" "$TMP/audio_$V.wav" "$SEED"
    fi
    for F in vertical carre; do
      case $F in vertical) S=1080:1920;; carre) S=1080:1080;; esac
      ffmpeg -loglevel error -y -framerate 30 -i "$TMP/f_${V}_${L}_${F}/f%04d.jpg" -i "$TMP/audio_$V.wav" \
        -vf "scale=$S:flags=lanczos,format=yuv420p" -c:v libx264 -preset veryfast -crf 20 \
        -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:a aac -b:a 160k -ar 44100 -shortest -movflags +faststart \
        "$OUT/tmp_${NAME}_${L}_${F}.mp4" && mv "$OUT/tmp_${NAME}_${L}_${F}.mp4" "$OUT/${NAME}_${L}_${F}.mp4"
      rm -rf "$TMP/f_${V}_${L}_${F}"
    done
  done
done
ls -la "$OUT"

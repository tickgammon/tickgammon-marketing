#!/bin/bash
# Fabrique la vidéo pub « Pack Sagesse » dans videos/packs/ (vertical 1080x1920, FR/EN/ES)
# Usage : bash generator/packs/build.sh
set -e
cd "$(dirname "$0")"
OUT="../../videos/packs"; TMP="/tmp/tgm_packs"; mkdir -p "$OUT" "$TMP"
V=sagesse; DUR=21.5; SEED=41
python3 - > "$TMP/ev_$V.json" <<'PY'
import json
ev={'pop':[],'click':[],'ting':[],'whoosh':[],'tada':[],'chime':[]}
def cut(t): ev['whoosh'].append(t-0.2)
ev['ting']+=[0.9,1.3]; cut(4.4); ev['click'].append(5.3); ev['pop']+=[[5.8,900],[7.4,1200],[7.8,1300]]
cut(9.2); ev['click'].append(10.1); ev['ting'].append(10.6); cut(14.0); ev['pop'].append([14.6,1000]); cut(17.8); ev['tada'].append(18.0); ev['chime'].append(18.6)
print(json.dumps(ev))
PY
python3 ../audio.py "$DUR" "$TMP/ev_$V.json" "$TMP/audio_$V.wav" "$SEED"
for L in fr en es; do node render.js "$V" "$L" "$TMP/f_${V}_${L}"; done
for L in fr en es; do
  ffmpeg -loglevel error -y -framerate 30 -i "$TMP/f_${V}_${L}/f%04d.jpg" -i "$TMP/audio_$V.wav" \
    -vf "scale=1080:1920:flags=lanczos,format=yuv420p" -c:v libx264 -preset medium -b:v 8M -maxrate 8M -bufsize 16M \
    -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:a aac -b:a 160k -ar 44100 -shortest -movflags +faststart \
    "$OUT/pack-sagesse-${L}.mp4"
  rm -rf "$TMP/f_${V}_${L}"
done
ls -la "$OUT"

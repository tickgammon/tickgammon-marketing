#!/bin/bash
# Fabrique les 4 vidéos de décembre 2026 dans videos/decembre/ (vertical 1080x1920, FR/EN/ES)
# Usage : bash generator/decembre/build.sh [avent plateau noel voeux]
set -e
cd "$(dirname "$0")"
OUT="../../videos/decembre"; TMP="/tmp/tgm_dec"; mkdir -p "$OUT" "$TMP"
for V in ${@:-avent plateau noel voeux}; do
  case $V in avent) DUR=13; SEED=21;; plateau) DUR=18; SEED=22;; noel) DUR=14; SEED=23;; voeux) DUR=15; SEED=24;; esac
  python3 - "$V" > "$TMP/ev_$V.json" <<'PY'
import json,sys
v=sys.argv[1]
ev={'pop':[],'click':[],'ting':[],'whoosh':[],'tada':[],'chime':[],'bells':[]}
def cut(t): ev['whoosh'].append(t-0.2); ev['pop']+=[[t+0.1,900],[t+0.35,1200]]
if v=='avent':
    ev['bells']+=[[0.2,1.8]]; ev['ting']+=[1.3,1.7]; cut(5); ev['pop']+=[[5.4+i*0.25,900+i*40] for i in range(10)]; cut(8.6); ev['chime'].append(9.4)
if v=='plateau':
    ev['bells']+=[[0.1,1.6]]; ev['whoosh'].append(0.3); ev['tada'].append(1.2); cut(4.2); ev['ting'].append(5.6); cut(9.2); ev['pop']+=[[9.6,800],[10.1,950]]; ev['ting']+=[10.5,10.8]; cut(13.6); ev['chime'].append(14.4)
if v=='noel':
    ev['bells']+=[[0.2,2.2]]; ev['chime'].append(0.9); cut(5); ev['tada'].append(5.6); cut(9.5); ev['bells']+=[[9.8,1.6]]; ev['chime'].append(10.4)
if v=='voeux':
    ev['ting']+=[1.0,1.4]; cut(5); ev['whoosh'].append(5.7); ev['tada'].append(6.4); ev['pop']+=[[6.6,1000],[6.9,1200]]; cut(10); ev['chime'].append(10.8)
print(json.dumps(ev))
PY
  python3 ../audio.py "$DUR" "$TMP/ev_$V.json" "$TMP/audio_$V.wav" "$SEED"
  for L in fr en es; do node render.js "$V" "$L" "$TMP/f_${V}_${L}" & done; wait
  for L in fr en es; do
    ffmpeg -loglevel error -y -framerate 30 -i "$TMP/f_${V}_${L}/f%04d.jpg" -i "$TMP/audio_$V.wav" \
      -vf "scale=1080:1920:flags=lanczos,format=yuv420p" -c:v libx264 -preset medium -b:v 8M -maxrate 8M -bufsize 16M \
      -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:a aac -b:a 160k -ar 44100 -shortest -movflags +faststart \
      "$OUT/${V}_${L}_vertical.mp4"
    rm -rf "$TMP/f_${V}_${L}"
  done
done
ls -la "$OUT"

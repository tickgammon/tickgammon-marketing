#!/bin/bash
# Fabrique les 3 vidéos de janvier 2027 dans videos/janvier2027/ (vertical 1080x1920, FR/EN/ES)
# Usage : bash generator/janvier2027/build.sh [galette soldes tournoi]
set -e
cd "$(dirname "$0")"
OUT="../../videos/janvier2027"; TMP="/tmp/tgm_jan"; mkdir -p "$OUT" "$TMP"
for V in ${@:-galette soldes tournoi}; do
  case $V in galette) DUR=14; SEED=31;; soldes) DUR=14; SEED=32;; tournoi) DUR=15; SEED=33;; esac
  python3 - "$V" > "$TMP/ev_$V.json" <<'PY'
import json,sys
v=sys.argv[1]
ev={'pop':[],'click':[],'ting':[],'whoosh':[],'tada':[],'chime':[],'bells':[]}
def cut(t): ev['whoosh'].append(t-0.2); ev['pop']+=[[t+0.1,900],[t+0.35,1200]]
if v=='galette':
    ev['bells']+=[[0.2,1.6]]; ev['click'].append(2.2); ev['ting']+=[2.6,2.9]; cut(5); ev['tada'].append(5.4); ev['chime'].append(6.1); cut(9.5); ev['chime'].append(10.3)
if v=='soldes':
    ev['bells']+=[[0.2,1.4]]; ev['tada'].append(0.6); cut(4.6); ev['pop']+=[[5.0,800],[5.5,950]]; ev['ting'].append(6.1); cut(9.5); ev['chime'].append(10.3)
if v=='tournoi':
    ev['whoosh'].append(0.2); ev['tada'].append(0.9); ev['ting'].append(1.4); cut(5); ev['chime'].append(5.9); cut(10); ev['tada'].append(10.6)
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

#!/bin/bash
# Fabrique les 2 vidéos Black Week 2026 dans videos/blackweek/ (vertical 1080x1920, FR/EN/ES)
# Usage : bash generator/blackweek/build.sh [bw bwfin]
set -e
cd "$(dirname "$0")"
OUT="../../videos/blackweek"; TMP="/tmp/tgm_bw"; mkdir -p "$OUT" "$TMP"
for V in ${@:-bw bwfin}; do
  case $V in bw) DUR=14; SEED=31;; bwfin) DUR=14; SEED=32;; esac
  python3 - "$V" > "$TMP/ev_$V.json" <<'PY'
import json,sys
v=sys.argv[1]
ev={'pop':[],'click':[],'ting':[],'whoosh':[],'tada':[],'chime':[]}
def cut(t): ev['whoosh'].append(t-0.2); ev['pop']+=[[t+0.1,900],[t+0.35,1200]]
ev['tada'].append(0.9); ev['ting']+=[1.3,1.6]; cut(4.6); ev['pop']+=[[5.4,850],[5.85,950],[6.3,1050]]; cut(9.6); ev['chime'].append(10.4)
print(json.dumps(ev))
PY
  python3 ../audio.py "$DUR" "$TMP/ev_$V.json" "$TMP/audio_$V.wav" "$SEED"
  for L in fr en es; do node render.js "$V" "$L" "$TMP/f_${V}_${L}"; done  # une langue à la fois (évite les délais dépassés)
  for L in fr en es; do
    ffmpeg -loglevel error -y -framerate 30 -i "$TMP/f_${V}_${L}/f%04d.jpg" -i "$TMP/audio_$V.wav" \
      -vf "scale=1080:1920:flags=lanczos,format=yuv420p" -c:v libx264 -preset medium -b:v 8M -maxrate 8M -bufsize 16M \
      -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:a aac -b:a 160k -ar 44100 -shortest -movflags +faststart \
      "$OUT/${V}_${L}_vertical.mp4"
    rm -rf "$TMP/f_${V}_${L}"
  done
done
ls -la "$OUT"

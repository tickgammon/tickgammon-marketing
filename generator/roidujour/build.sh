#!/bin/bash
# Fabrique le kit vidéo « Roi du jour » dans videos/roidujour/
#   launch : vidéo de lancement 24 s (FR/EN/ES × vertical, carré, paysage)
#   teaser : teaser 9,5 s (FR/EN/ES × vertical, carré)
# Usage : bash generator/roidujour/build.sh [launch|teaser ...]
set -e
cd "$(dirname "$0")"
OUT="../../videos/roidujour"; TMP="/tmp/tgm_roi"; mkdir -p "$OUT" "$TMP"
VIDS="${@:-launch teaser}"
for V in $VIDS; do
  case $V in
    launch) DUR=24; SEED=11; FMTS="vertical carre paysage"; NAME=roidujour;;
    teaser) DUR=9.5; SEED=12; FMTS="vertical carre"; NAME=teaser_roidujour;;
  esac
  python3 - "$V" > "$TMP/ev_$V.json" <<'EOF'
import json,sys
v=sys.argv[1]
ev={'pop':[],'click':[],'ting':[],'whoosh':[],'tada':[],'chime':[]}
def cuts(ts):
    for t in ts: ev['whoosh'].append(t-0.2); ev['pop']+=[[t+0.1,900],[t+0.35,1200]]
if v=='launch':
    ev['pop']+=[[0.4,700],[0.6,1000],[0.9,1100]]; ev['ting']+=[1.7]
    cuts([3.6,8.8,13.2])
    ev['pop']+=[[5.4,900],[6.2,1050],[7.0,1200]]; ev['ting']+=[7.6]
    ev['pop']+=[[9.4+i*0.4,1000+i*90] for i in range(4)]
    ev['whoosh'].append(14.2); ev['tada'].append(15.3); ev['ting']+=[16.2]
    ev['whoosh'].append(19.6); ev['pop']+=[[20.1,900],[20.5,1150]]; ev['ting']+=[21.2]; ev['chime'].append(22.8)
if v=='teaser':
    ev['pop']+=[[0.15,700],[0.4,1000]]; ev['ting']+=[1.4,2.8,3.9]
    ev['whoosh'].append(4.8); ev['tada'].append(5.3); ev['chime'].append(8.3)
print(json.dumps(ev))
EOF
  python3 ../audio.py "$DUR" "$TMP/ev_$V.json" "$TMP/audio_$V.wav" "$SEED"
  for L in fr en es; do
    for F in $FMTS; do node render.js "$V" "$L" "$F" "$TMP/f_${V}_${L}_${F}" & done; wait
    for F in $FMTS; do
      case $F in vertical) S=1080:1920;; carre) S=1080:1080;; paysage) S=1920:1080;; esac
      ffmpeg -loglevel error -y -framerate 30 -i "$TMP/f_${V}_${L}_${F}/f%04d.jpg" -i "$TMP/audio_$V.wav" \
        -vf "scale=$S:flags=lanczos,format=yuv420p" -c:v libx264 -preset medium -crf 22 \
        -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:a aac -b:a 160k -ar 44100 -shortest -movflags +faststart \
        "$OUT/${NAME}_${L}_${F}.mp4"
      rm -rf "$TMP/f_${V}_${L}_${F}"
    done
  done
done
ls -la "$OUT"

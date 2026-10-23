#!/bin/bash
# Fabrique le kit vidéo « Face à face » dans videos/facetoface/
#   launch : vidéo de lancement 24 s (FR/EN/ES × vertical, carré, paysage)
#   teaser : teaser 9,5 s (FR/EN/ES × vertical, carré)
#   howto  : Short « Comment lancer une partie » 20,5 s (FR/EN/ES × vertical)
# Usage : bash generator/facetoface/build.sh [launch|teaser|howto ...]
set -e
cd "$(dirname "$0")"
OUT="../../videos/facetoface"; TMP="/tmp/tgm_ff"; mkdir -p "$OUT" "$TMP"
VIDS="${@:-launch teaser howto}"
for V in $VIDS; do
  case $V in
    launch) DUR=24; SEED=5; FMTS="vertical carre paysage"; NAME=facetoface;;
    teaser) DUR=9.5; SEED=8; FMTS="vertical carre"; NAME=teaser_facetoface;;
    howto)  DUR=20.5; SEED=3; FMTS="vertical"; NAME=howto_facetoface;;
  esac
  python3 - "$V" > "$TMP/ev_$V.json" <<'EOF'
import json,sys
v=sys.argv[1]
ev={'pop':[],'click':[],'ting':[],'whoosh':[],'tada':[],'chime':[]}
def cuts(ts):
    for t in ts: ev['whoosh'].append(t-0.2); ev['pop']+=[[t+0.1,900],[t+0.35,1200]]
if v=='launch':
    ev['pop']+=[[0.4,700],[0.6,1000],[0.9,1100]]; ev['ting']+=[1.7]
    cuts([3.6,8.4,12.6,16.4]); ev['click']+=[3.9+k*0.05 for k in range(6)]
    ev['ting']+=[9.6,10.4]; ev['pop']+=[[12.6+0.5+i*0.35,1000+i*80] for i in range(5)]
    ev['pop']+=[[16.4+0.3+i*0.25,900+i*120] for i in range(3)]; ev['ting']+=[17.7]
    ev['whoosh'].append(19.4); ev['tada'].append(19.65); ev['ting']+=[20.9]; ev['chime'].append(22.8)
if v=='teaser':
    ev['pop']+=[[0.15,700],[0.4,1000]]; ev['ting']+=[1.2,2.6,3.8]
    ev['whoosh'].append(4.8); ev['tada'].append(5.1); ev['chime'].append(8.3)
if v=='howto':
    ev['pop']+=[[0.4,700],[0.6,1000],[0.9,1100]]; ev['ting']+=[1.7]
    cuts([3.2,7.0,10.8,14.4]); ev['click']+=[3.2+1.4,3.2+1.45]
    ev['click']+=[7.0+0.9+k*0.3 for k in range(3)]; ev['click']+=[14.4+1.2+k*0.045 for k in range(7)]
    ev['whoosh'].append(17.0); ev['tada'].append(17.25); ev['ting']+=[18.5]; ev['chime'].append(19.4)
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

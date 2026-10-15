#!/bin/bash
# Fabrique les 12 vidéos d'un sujet (3 langues x 4 formats) dans videos/<NN>_<sujet>/
# Usage : bash generator/build.sh <sujet>      (ex. bash generator/build.sh regles)
set -e
cd "$(dirname "$0")"
SID="$1"; [ -z "$SID" ] && { echo "usage: build.sh <sujet>"; exit 1; }
NUM=$(python3 -c "import json;print('%02d'%[s for s in json.load(open('subjects.json')) if s['id']=='$SID'][0]['num'])")
SEED=$(python3 -c "import json;print([s for s in json.load(open('subjects.json')) if s['id']=='$SID'][0]['seed'])")
GRID=$(python3 -c "import json;s=[s for s in json.load(open('subjects.json')) if s['id']=='$SID'][0];print(1 if s['facts'][0]['vis']['type']=='grid' else 0)")
DICE=$(python3 -c "import json;s=[s for s in json.load(open('subjects.json')) if s['id']=='$SID'][0];print(','.join(str(i) for i,f in enumerate(s['facts']) if f['vis']['type']=='dice'))")
OUT="../videos/${NUM}_${SID}"; TMP="/tmp/tgm_${SID}"; mkdir -p "$OUT" "$TMP"
# bande son (identique pour les 12 vidéos du sujet)
python3 - "$GRID" "$DICE" > "$TMP/ev.json" <<'EOF'
import json,sys
grid=sys.argv[1]=='1'; dice=[int(x) for x in sys.argv[2].split(',') if x]
T0,FD,TIP0,OUT0=3.5,3.2,16.3,19.0
ev={'pop':[[0.1,700],[0.5,1100],[0.7,900],[1.0,1000]],'click':[],'ting':[1.6],'whoosh':[T0-0.25],'tada':[TIP0+0.05],'chime':[24.0]}
for i in range(4):
    s=T0+i*FD; ev['pop']+= [[s+0.15,900+i*100],[s+0.4,1200]]
    if i>0: ev['whoosh'].append(s-0.2)
    if grid and i==0: ev['click']+= [s+0.2+k*0.035 for k in range(36)]
    if i in dice: ev['click']+= [s+0.6+k*0.045 for k in range(7)]+[s+0.9+k*0.045 for k in range(6)]
ev['ting']+=[TIP0+0.8,OUT0+1.3,OUT0+4.4]; ev['whoosh']+=[TIP0-0.2,OUT0-0.2]
ev['pop']+=[[OUT0+0.1,700],[OUT0+0.35,900],[OUT0+0.65,1000],[OUT0+1.05,1100]]
print(json.dumps(ev))
EOF
python3 audio.py 25 "$TMP/ev.json" "$TMP/audio.wav" "$SEED"
# images + encodage, 4 formats en parallèle par langue
for L in fr en es; do
  for F in vertical portrait carre paysage; do node render.js "$SID" "$L" "$F" "$TMP/f_${L}_${F}" & done; wait
  for F in vertical portrait carre paysage; do
    case $F in vertical) S=1080:1920;; portrait) S=1080:1350;; carre) S=1080:1080;; paysage) S=1920:1080;; esac
    ffmpeg -loglevel error -y -framerate 30 -i "$TMP/f_${L}_${F}/f%04d.jpg" -i "$TMP/audio.wav" \
      -vf "scale=$S:flags=lanczos,format=yuv420p" -c:v libx264 -preset medium -crf 22 \
      -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:a aac -b:a 160k -ar 44100 -shortest -movflags +faststart \
      "$OUT/${SID}_${L}_${F}.mp4" &
  done; wait
  rm -rf "$TMP"/f_${L}_*
done
ls -la "$OUT"

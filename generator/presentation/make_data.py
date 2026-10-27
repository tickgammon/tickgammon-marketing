# 27/10/2026 — Fabrique data_<partie>.json (décalage de la voix, durée, sous-titres, enveloppe pour la chouette).
# Usage : python3 make_data.py <partie> <voix.mp3> <decalage_voix> <marge_fin> subs.json
import json, sys, subprocess, numpy as np
part, mp3, V, tail, subsf = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
a = np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',mp3,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout,np.int16).astype(float)
dv = len(a) / 16000; dur = round(V + dv + tail, 2)
h = 16000 // 30; n = int(dur * 30); env = []
for i in range(n):
    j = int((i / 30 - V) * 16000)
    env.append(0.0 if j < 0 or j + h > len(a) else float(np.sqrt(np.mean(a[j:j+h]**2))))
m = np.percentile([e for e in env if e > 0] or [1], 95)
env = [round(min(1, e / m), 3) for e in env]
subs = [[round(s[0] + V, 2), round(s[1] + V, 2), s[2]] for s in json.load(open(subsf))]
json.dump({'voice': V, 'dur': dur, 'subs': subs, 'env': env}, open(f'data_{part}.json', 'w'), ensure_ascii=False)
print(part, 'dur', dur)

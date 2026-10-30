# 25/10/2026 — Fichier de sous-titres .srt pour YouTube (à ajouter dans Studio → Sous-titres, désactivés par défaut).
# Même découpage que les anciens sous-titres incrustés de lecon.html. Usage : python3 srt.py fr|en|es [sortie.srt]
import json, re, sys
lang = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else f'lecon_{lang}.srt'
tl = json.load(open(f'timeline_{lang}.json', encoding='utf-8'))['tl']
def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'
cues = []
for x in tl:
    parts = re.findall(r'[^.!?…]+[.!?…]+[»"]?\s*|[^.!?…]+$', x['txt']) or [x['txt']]
    chunks, cur = [], ''
    for p in parts:
        if len(cur + p) > 105 and cur: chunks.append(cur.strip()); cur = p
        else: cur += p
    if cur.strip(): chunks.append(cur.strip())
    tot = sum(len(c) for c in chunks); acc = 0
    for c in chunks:
        a = x['t0'] + x['d'] * acc / tot; acc += len(c); b = x['t0'] + x['d'] * acc / tot
        cues.append((a, b + 0.3, c))
with open(out, 'w', encoding='utf-8') as f:
    for i, (a, b, c) in enumerate(cues, 1):
        f.write(f'{i}\n{ts(a)} --> {ts(b)}\n{c}\n\n')
print(out, len(cues), 'sous-titres')

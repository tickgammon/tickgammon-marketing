# 27/10/2026 — Musique originale « bande-annonce » de la vidéo de présentation (partie 1 : ouverture).
# Intro calme (bourdon + cordes) → impact sur le titre → ostinato qui monte → montée finale + impact.
# Usage : python3 pres_music.py data_p1.json music_p1.wav
import numpy as np, json, sys
from scipy.io import wavfile
from scipy.signal import butter, lfilter, fftconvolve
SR = 44100
D = json.load(open(sys.argv[1])); out = sys.argv[2]
V, DUR = D['voice'], D['dur']
N = int(SR * (DUR + 0.6))
rng = np.random.default_rng(11)
def t_(d): return np.arange(int(SR * d)) / SR
def f(n): return 440 * 2 ** ((n - 69) / 12)
def lp(x, fc, o=2): b, a = butter(o, min(fc, SR/2-100) / (SR / 2)); return lfilter(b, a, x)
def hp(x, fc, o=2): b, a = butter(o, fc / (SR / 2), 'high'); return lfilter(b, a, x)
def saw(fr, t, ph=0): return 2 * ((fr * t + ph) % 1) - 1
def add(buf, start, sig, g=1.0):
    i = int(start * SR)
    if i >= len(buf) or i + len(sig) <= 0: return
    if i < 0: sig = sig[-i:]; i = 0
    j = min(len(buf), i + len(sig)); buf[i:j] += sig[:j - i] * g
def ramp(t0, t1, a, b, n=N):
    x = np.arange(n) / SR; return a + (b - a) * np.clip((x - t0) / (t1 - t0), 0, 1)

beat = 60 / 90; bar = 4 * beat
prog = [(38, [62, 65, 69]), (34, [62, 65, 70]), (41, [60, 65, 69]), (36, [60, 64, 67])]  # Rém, Sib, Fa, Do
strings = np.zeros(N); low = np.zeros(N); perc = np.zeros(N); fx = np.zeros(N)

# cordes (pad soyeux) + bourdon grave, sur toute la partie
k = 0; tt = 0.0
while tt < DUR + 0.6:
    root, ch = prog[k % 4]; d = bar * 2
    t = t_(d); s = np.zeros(len(t))
    for n in ch + [n + 12 for n in ch[:1]]:
        for det in (-0.1, 0, 0.1): s += saw(f(n) * 2 ** (det / 12), t, rng.random())
    e = np.minimum(1, t / 0.9) * np.minimum(1, np.maximum(0, d - t) / 0.6)
    add(strings, tt, lp(s, 1500) * e / 12)
    dr = (np.sin(2 * np.pi * f(root - 12) * t) + 0.5 * saw(f(root - 12), t)) * e
    add(low, tt, lp(dr, 260) * 0.55)
    tt += d; k += 1
strings = strings * ramp(0, 4.2, 0.35, 1.0)
# ostinato grave (violoncelles staccato) à partir du titre, qui s'intensifie
ost = np.zeros(N); tt = 4.2; i = 0
while tt < DUR:
    root = prog[int(tt // (bar * 2)) % 4][0]
    n = root + (12 if i % 4 == 3 else 0)
    t = t_(beat / 2); s = saw(f(n), t) + saw(f(n) * 1.004, t)
    add(ost, tt, lp(s, 900 + 1400 * min(1, (tt - 4.2) / (DUR - 4.2))) * np.exp(-t / 0.11) * 0.35)
    tt += beat / 2; i += 1
ost *= ramp(4.2, DUR - 1, 0.35, 1.0)
# percussions
def boom(d=2.2):
    t = t_(d); fr = 70 * np.exp(-t * 6) + 32
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.7)
def timp(n=38, d=1.6):
    t = t_(d); s = np.sin(2 * np.pi * f(n) * t * (1 + 0.02 * np.exp(-t * 20))) + 0.4 * np.sin(2 * np.pi * f(n) * 1.5 * t)
    s += lp(rng.standard_normal(len(t)), 400) * np.exp(-t / 0.05) * 0.6
    return s * np.exp(-t / 0.45)
def kick():
    t = t_(0.4); fr = 120 * np.exp(-t * 22) + 42
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.18)
def crash(d=3.0):
    t = t_(d); return hp(rng.standard_normal(len(t)), 3500) * np.exp(-t / 0.9) * 0.35
def tom(n):
    t = t_(0.5); fr = f(n) * (1 + 0.5 * np.exp(-t * 30))
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.18)
def whoosh(d=0.9, up=True):
    t = t_(d); s = rng.standard_normal(len(t)); out = np.zeros(len(t))
    for a in range(0, len(t), 512):  # balayage de filtre
        p = a / len(t); fc = 300 + (5000 if up else 3000) * (p if up else 1 - p)
        seg_ = s[max(0, a - 2048):a + 512]; out[a:a + 512] = lp(seg_, fc)[-len(out[a:a + 512]):]
    return out * np.sin(np.pi * t / d) ** 2 * 0.5
# impact du titre
add(perc, 4.2, boom(), 1.0); add(perc, 4.2, timp(38), 0.7); add(fx, 4.2, crash(), 0.8)
add(fx, 1.6, whoosh(1.4), 0.9)  # vol de la chouette
add(fx, 3.4, whoosh(0.8), 0.6)
# battements « cœur » (kick) de plus en plus présents
tt = 8.0
while tt < V + 19.6:
    add(perc, tt, kick(), 0.35 + 0.35 * min(1, (tt - 8) / 12)); tt += beat * 2
# cartes présidents / organisateurs / joueurs
for i, t0 in enumerate([V + 13.3, V + 14.5, V + 15.7]):
    add(perc, t0, timp(38 + [0, 3, 7][i]), 0.55); add(fx, t0 - 0.35, whoosh(0.5), 0.4)
# sommaire : batterie pleine + toms, montée finale
tt = V + 19.6; i = 0
while tt < DUR - 0.2:
    add(perc, tt, kick(), 0.75)
    if i % 2 == 1: add(perc, tt, tom(45 - (i % 4)), 0.35)
    tt += beat / 2 if tt > DUR - 3 else beat; i += 1
for k_ in range(8): add(fx, V + 20.0 + k_ * 0.32 - 0.12, whoosh(0.35), 0.25)
rt = t_(DUR - (V + 19.6)); riser = rng.standard_normal(len(rt))
riser = hp(riser, 800) * (rt / rt[-1]) ** 2.2 * 0.45
tone = np.sin(2 * np.pi * np.cumsum(110 * 2 ** (rt / rt[-1] * 2)) / SR) * (rt / rt[-1]) ** 2 * 0.25
add(fx, V + 19.6, riser + tone)
add(perc, DUR - 0.05, boom(1.0), 1.0); add(fx, DUR - 0.05, crash(0.8), 0.6)

mix = strings * 0.9 + low * 0.9 + ost * 0.8 + perc * 0.9 + fx * 0.8
ir = rng.standard_normal(int(SR * 2.2)) * np.exp(-np.arange(int(SR * 2.2)) / (SR * 0.55)) * 0.02
wet = fftconvolve(mix, ir)[:N]
mix = mix + wet * 0.6
fade = np.ones(N); fade[:int(SR * 0.8)] = np.linspace(0, 1, int(SR * 0.8))
mix *= fade; mix /= np.max(np.abs(mix)) + 1e-9; mix = np.tanh(mix * 1.3) / np.tanh(1.3) * 0.9
wavfile.write(out, SR, (np.stack([mix, np.roll(mix, 220)], 1) * 32767).astype(np.int16))
print('ok', out, round(len(mix) / SR, 2))

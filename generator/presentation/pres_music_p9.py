# 27/10/2026 — Musique originale de la vidéo de présentation, partie 9 « Appel aux clubs » (final épique, impact sur le logo puis silence).
# Suite de la partie 1 (même tonalité, même tempo) : nappes + ostinato, puis un beat léger à partir de l accueil, tintements sur chaque élément montré, montée et impact sur « les clubs ».
# Usage : python3 pres_music_p9.py data_p9.json music_p9.wav
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
def hat(d=0.08):
    t = t_(d); return hp(rng.standard_normal(len(t)), 7000) * np.exp(-t / 0.02)
def clap():
    t = t_(0.3); n = lp(hp(rng.standard_normal(len(t)), 900), 5000)
    e = np.exp(-t / 0.07) + 0.6 * np.exp(-np.maximum(0, t - 0.012) / 0.01) * (t > 0.012)
    return n * e * 0.6
def crash(d=3.0):
    t = t_(d); return hp(rng.standard_normal(len(t)), 3500) * np.exp(-t / 0.9) * 0.35
def bell(n, d=1.4):
    t = t_(d); s = sum(a * np.sin(2 * np.pi * f(n) * m * t) for m, a in ((1, 1), (2.76, .35), (5.4, .15)))
    return s * np.exp(-t / 0.35) * np.minimum(1, t / 0.003)
def whoosh(d=0.9):
    t = t_(d); s = rng.standard_normal(len(t)); out = np.zeros(len(t))
    for a in range(0, len(t), 512):
        fc = 300 + 5000 * a / len(t)
        seg_ = s[max(0, a - 2048):a + 512]; out[a:a + 512] = lp(seg_, fc)[-len(out[a:a + 512]):]
    return out * np.sin(np.pi * t / d) ** 2 * 0.5

strings = np.zeros(N); low = np.zeros(N); perc = np.zeros(N); fx = np.zeros(N); ost = np.zeros(N)
k = 0; tt = 0.0
while tt < DUR + 0.6:
    root, ch = prog[k % 4]; d = bar * 2
    t = t_(d); s = np.zeros(len(t))
    for n in ch + [ch[0] + 12]:
        for det in (-0.1, 0, 0.1): s += saw(f(n) * 2 ** (det / 12), t, rng.random())
    e = np.minimum(1, t / 0.6) * np.minimum(1, np.maximum(0, d - t) / 0.6)
    add(strings, tt, lp(s, 1700) * e / 12)
    add(low, tt, lp((np.sin(2 * np.pi * f(root - 12) * t) + 0.5 * saw(f(root - 12), t)) * e, 260) * 0.55)
    tt += d; k += 1
# ostinato continu (repris de la fin de la partie 1)
tt = 0.0; i = 0
while tt < DUR:
    root = prog[int(tt // (bar * 2)) % 4][0]; n = root + (12 if i % 4 == 3 else 0)
    t = t_(beat / 2); s = saw(f(n), t) + saw(f(n) * 1.004, t)
    add(ost, tt, lp(s, 1400 + 900 * min(1, tt / DUR)) * np.exp(-t / 0.11) * 0.35)
    tt += beat / 2; i += 1
ost *= ramp(0, 3, 0.6, 1.0)
def choir(n, d):
    t = t_(d); v = np.zeros(len(t))
    for h, g in ((1, 1), (2, .5), (3, .3), (4, .18), (5, .1)):
        for det in (-0.15, 0, 0.15): v += g * np.sin(2 * np.pi * f(n) * h * 2 ** (det / 12) * t * (1 + 0.004 * np.sin(2 * np.pi * 5 * t)))
    return lp(v, 2200) * np.minimum(1, t / 0.4) * np.minimum(1, np.maximum(0, d - t) / 0.5) * 0.08
LOGO = V + 23.3
add(perc, 0.0, boom(1.6), 0.7); add(fx, 0.0, crash(2.0), 0.5)
k = 0; tt = 0.0
while tt < LOGO + 3:
    root, ch = prog[k % 4]
    for n in ch: add(fx, tt, choir(n, bar * 2), 0.9 if tt > V + 12 else 0.6)
    tt += bar * 2; k += 1
tt = 0.0; b = 0
while tt < LOGO - 0.1:
    big_ = tt > V + 13.1
    add(perc, tt, kick(), 0.75 if big_ else 0.55)
    if b % 2 == 1: add(perc, tt, clap(), 0.45 if big_ else 0.3)
    for k_ in range(2): add(perc, tt + k_ * beat / 2, hat(), 0.12)
    if big_: add(perc, tt + beat / 2, timp(38 if b % 2 else 33, 0.6), 0.3)
    root = prog[int(tt // (bar * 2)) % 4][0]
    tb = t_(beat * 0.9); add(low, tt, lp(saw(f(root - 12), tb) * np.exp(-tb / 0.25), 500) * 0.5)
    tt += beat; b += 1
add(perc, V + 2.6, timp(38), 0.6)
for i, t0 in enumerate([4.92, 6.6, 8.3]): add(perc, V + t0, timp([38, 41, 45][i]), 0.6); add(fx, V + t0 + 1.0, bell(79 + i * 3, 0.6), 0.15)
add(perc, V + 13.13, boom(), 1.0); add(fx, V + 13.13, crash(), 0.8)
for i in range(3): add(fx, V + 18.1 + i * 0.4, bell(74 + i * 5 + 12, 0.6), 0.15)
T0 = V + 20.0
rt = t_(LOGO - T0); riser = hp(rng.standard_normal(len(rt)), 800) * (rt / rt[-1]) ** 2.2 * 0.5
tone = np.sin(2 * np.pi * np.cumsum(110 * 2 ** (rt / rt[-1] * 2)) / SR) * (rt / rt[-1]) ** 2 * 0.28
add(fx, T0, riser + tone)
add(perc, LOGO, boom(3.0), 1.0); add(perc, LOGO, timp(36, 2.5), 0.9); add(fx, LOGO, crash(4.0), 1.0)
T1 = LOGO
strings *= ramp(T1, T1 + 0.1, 1.0, 1.2)
for arr in (strings, low, ost): arr *= ramp(LOGO + 0.2, DUR - 0.2, 1.0, 0.0)
mix = (strings * 0.9 + low * 0.9 + ost * 0.8 + perc * 0.9 + fx * 0.8) * ramp(DUR - 2.4, DUR - 0.3, 1.0, 0.0)
ir = rng.standard_normal(int(SR * 2.2)) * np.exp(-np.arange(int(SR * 2.2)) / (SR * 0.55)) * 0.02
mix = mix + fftconvolve(mix, ir)[:N] * 0.6
mix /= np.max(np.abs(mix)) + 1e-9; mix = np.tanh(mix * 1.3) / np.tanh(1.3) * 0.9
wavfile.write(out, SR, (np.stack([mix, np.roll(mix, 220)], 1) * 32767).astype(np.int16))
print('ok', out, round(len(mix) / SR, 2))

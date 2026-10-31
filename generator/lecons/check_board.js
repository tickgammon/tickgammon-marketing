// Contrôle automatique des plateaux d'une leçon de la chouette (règles de Joyce, 31/10/2026)
// Usage : node check_board.js leconN.html [timeline.json]
// Vérifie, pour chaque scène avec plateau, à de nombreux instants :
//  1. 15 pions par couleur (plateau + barre + sortis) ;
//  2. Blanc avance du point 24 vers le point 1 (index qui diminue), Noir dans l'autre sens ;
//  3. sorties : Blanc uniquement depuis son jan (points 1-6) et seulement quand ses 15 pions sont rentrés/sortis ;
//     Noir depuis ses points 1-6 (index 18-23) ;
//  4. arcs/flèches arc(f,t) : même sens que la couleur du pion de départ ; une flèche de sortie blanche
//     doit arriver EN BAS à droite.
const { chromium } = require('/opt/npm-tools/node_modules/playwright');
const fs = require('fs'), path = require('path');
const [htmlFile, tlFile = 'timeline.json'] = process.argv.slice(2);
if (!htmlFile) { console.error('usage: node check_board.js leconN.html [timeline.json]'); process.exit(2); }
(async () => {
  const dir = path.dirname(path.resolve(htmlFile));
  const data = fs.readFileSync(path.resolve(dir, tlFile), 'utf8');
  let html = fs.readFileSync(htmlFile, 'utf8');
  html = html.replace('<script>\nconst $', `<script>window.DATA=${data};window.LANG='fr';</script><script>\nconst $`);
  const tmp = path.join(dir, '_check.html'); fs.writeFileSync(tmp, html);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + tmp, { waitUntil: 'load' }); await p.waitForTimeout(300);
  const res = await p.evaluate(() => {
    const out = [];
    const add = (sc, t, msg) => out.push({ sc, t: +t.toFixed(2), msg });
    const total = (s, c) => { let n = 0; for (const v of s.p) n += c === 'w' ? Math.max(0, v) : Math.max(0, -v); return n + (c === 'w' ? s.barW + s.offW : s.barB + s.offB); };
    const owner = (s, i) => (typeof i !== 'number' ? null : s.p[i] > 0 ? 'w' : s.p[i] < 0 ? 'b' : null);
    const allHome = (s, c) => { for (let i = 0; i < 24; i++) { const v = s.p[i]; if (c === 'w' && v > 0 && i > 5) return false; if (c === 'b' && v < 0 && i < 18) return false; } return (c === 'w' ? s.barW : s.barB) === 0; };
    let arcs = [];
    const realArc = window.arc;
    if (realArc) window.arc = function (f, t, ...r) { const o = realArc(f, t, ...r); arcs.push({ f, t, d: o.d }); return o; };
    for (const cur of TL) {
      const D = cur.d, fn = SC[cur.p]; if (!fn) continue;
      for (let lt = 0; lt <= D; lt += Math.max(.1, D / 40)) {
        arcs = [];
        const Fx = { board: null, owl: null, ov: '', top: 1, note: null };
        try { fn(lt, D, Fx); } catch (e) { add(cur.p, lt, 'ERREUR JS ' + e.message); continue; }
        const o = Fx.board; if (!o) continue;
        const base = o.st || newState();
        for (const c of ['w', 'b']) { const n = total(base, c); if (n !== 15) add(cur.p, lt, `${c === 'w' ? 'Blancs' : 'Noirs'} : ${n} pions au lieu de 15`); }
        // mouvements dans l'ordre
        const mv = (o.mv || []).filter(Boolean); // même ordre que applyMoves()
        let s = clone(base);
        for (const m of mv) {
          const nm = `${m.c === 'w' ? 'Blanc' : 'Noir'} ${typeof m.f === 'number' ? (m.c === 'w' ? m.f + 1 : 24 - m.f) : m.f}→${typeof m.t === 'number' ? (m.c === 'w' ? m.t + 1 : 24 - m.t) : m.t}`;
          if (m.f !== 'bar' && m.f !== 'off' && cnt(s, m.c, m.f) < 1) add(cur.p, lt, `${nm} : aucun pion de cette couleur au départ`);
          if (m.t === 'off') {
            if (m.c === 'w' && !(m.f <= 5)) add(cur.p, lt, `${nm} : sortie blanche hors du jan (points 1-6)`);
            if (m.c === 'b' && !(m.f >= 18)) add(cur.p, lt, `${nm} : sortie noire hors de son jan`);
            if (!allHome(s, m.c)) add(cur.p, lt, `${nm} : sortie alors que des pions ne sont pas rentrés`);
          } else if (m.t === 'bar') { /* pion frappé : pas de sens imposé */ }
          else if (m.f === 'bar') { if (m.c === 'w' && m.t < 18) add(cur.p, lt, `${nm} : entrée blanche hors du jan adverse`); if (m.c === 'b' && m.t > 5) add(cur.p, lt, `${nm} : entrée noire hors du jan adverse`); }
          else if (m.c === 'w' && !(m.f > m.t)) add(cur.p, lt, `${nm} : le Blanc recule (doit aller vers le point 1)`);
          else if (m.c === 'b' && !(m.f < m.t)) add(cur.p, lt, `${nm} : le Noir recule`);
          if (m.f !== 'bar' && m.f !== 'off' && cnt(s, m.c, m.f) >= 1) { take(s, m.c, m.f); put(s, m.c, m.t); }
        }
        // arcs : couleur = pion sur la case de départ (état de base ou après mouvements)
        for (const a of arcs) {
          const c = owner(base, a.f) || owner(s, a.f) || 'w';
          const nm = `flèche ${c === 'w' ? 'blanche' : 'noire'} ${c === 'w' ? a.f + 1 : 24 - a.f}→${a.t === 'off' ? 'off' : (c === 'w' ? a.t + 1 : 24 - a.t)}`;
          if (a.t === 'off') {
            const y2 = +a.d.trim().split(/\s+/).pop();
            if (c === 'w' && !(y2 > BH / 2)) add(cur.p, lt, `${nm} : arrive en HAUT à droite (la sortie blanche est en bas à droite)`);
            if (c === 'w' && a.f > 5) add(cur.p, lt, `${nm} : sortie directe depuis l'extérieur du jan`);
          } else if (typeof a.t === 'number') {
            if (c === 'w' && !(a.f > a.t)) add(cur.p, lt, `${nm} : flèche dans le mauvais sens`);
            if (c === 'b' && !(a.f < a.t)) add(cur.p, lt, `${nm} : flèche dans le mauvais sens`);
          }
        }
      }
    }
    return out;
  });
  await b.close(); fs.unlinkSync(tmp);
  const seen = new Map();
  for (const r of res) { const k = r.sc + '|' + r.msg; if (!seen.has(k)) seen.set(k, r); }
  for (const e of errs) console.log('ERREUR PAGE', e);
  if (!seen.size) { console.log('OK : 0 violation'); return; }
  for (const r of seen.values()) console.log(`${r.sc} (t≈${r.t}s) : ${r.msg}`);
  console.log(`${seen.size} violation(s)`); process.exitCode = 1;
})();

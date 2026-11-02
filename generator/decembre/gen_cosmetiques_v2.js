// Génère les cosmétiques de Noël 2026 (TickGammon) — rendu Chromium (Playwright)
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const OUT = path.resolve(__dirname, '..');
const CK = path.resolve(__dirname, '../../cosmetiques/apercus_png');
const OWL = 'data:image/png;base64,' + fs.readFileSync(path.join(__dirname, 'owl_full.png')).toString('base64');
const FONT = 'data:font/woff2;base64,' + fs.readFileSync('/home/claude/tickgammon-marketing/generator/lecons/brico800.woff2').toString('base64');

// Flocon à 6 branches (symétrique : supporte les rotations)
function flake(cx, cy, r, stroke, sw, extra = '') {
  let s = `<g transform="translate(${cx},${cy})" stroke="${stroke}" stroke-width="${sw}" stroke-linecap="round" fill="none" ${extra}>`;
  for (let k = 0; k < 6; k++) {
    s += `<g transform="rotate(${k * 60})">
      <line x1="0" y1="0" x2="0" y2="${-r}"/>
      <line x1="0" y1="${-r * .45}" x2="${-r * .2}" y2="${-r * .62}"/><line x1="0" y1="${-r * .45}" x2="${r * .2}" y2="${-r * .62}"/>
      <line x1="0" y1="${-r * .7}" x2="${-r * .16}" y2="${-r * .84}"/><line x1="0" y1="${-r * .7}" x2="${r * .16}" y2="${-r * .84}"/>
      <line x1="0" y1="${-r * .22}" x2="${-r * .12}" y2="${-r * .3}"/><line x1="0" y1="${-r * .22}" x2="${r * .12}" y2="${-r * .3}"/></g>`;
  }
  return s + `<circle r="${r * .07}" fill="${stroke}" stroke="none"/></g>`;
}
// étoile à 8 branches
function star8(cx, cy, R, r, fill) {
  let p = []; for (let i = 0; i < 16; i++) { const a = Math.PI / 8 * i - Math.PI / 2, rr = i % 2 ? r : R; p.push((cx + rr * Math.cos(a)).toFixed(1) + ',' + (cy + rr * Math.sin(a)).toFixed(1)); }
  return `<polygon points="${p.join(' ')}" fill="${fill}"/>`;
}
function rnd(seed) { let s = seed; return () => (s = (s * 16807) % 2147483647) / 2147483647; }

// ---------- 1. Pion « Pions hiver » (600×600, fond blanc) ----------
function checkerHiver() {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <defs>
   <radialGradient id="ice" cx="42%" cy="38%" r="70%"><stop offset="0" stop-color="#ffffff"/><stop offset=".55" stop-color="#eaf5fb"/><stop offset="1" stop-color="#b9d8e8"/></radialGradient>
   <linearGradient id="rim" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#cfe4ef"/><stop offset="1" stop-color="#8fb6cc"/></linearGradient>
   <radialGradient id="in" cx="50%" cy="50%" r="55%"><stop offset="0" stop-color="#f7fbfd"/><stop offset="1" stop-color="#d6eaf4"/></radialGradient>
  </defs>
  <rect width="600" height="600" fill="#fff"/>
  <circle cx="300" cy="300" r="296" fill="url(#rim)"/>
  <circle cx="300" cy="300" r="282" fill="url(#ice)"/>
  <circle cx="300" cy="300" r="228" fill="url(#in)" stroke="#a9cbdd" stroke-width="5"/>
  <circle cx="300" cy="300" r="246" fill="none" stroke="#ffffff" stroke-width="4" stroke-dasharray="2 16" stroke-linecap="round"/>
  ${flake(300, 300, 170, '#5d93b3', 15)}
  ${flake(300, 300, 170, '#ffffff', 5)}
  <ellipse cx="225" cy="190" rx="95" ry="45" fill="#fff" opacity=".45" transform="rotate(-35 225 190)"/>
  </svg>`;
}
// ---------- 2. Pion « Sapin » (sombre) ----------
function checkerSapin() {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600" viewBox="0 0 600 600">
  <defs>
   <radialGradient id="g" cx="40%" cy="35%" r="75%"><stop offset="0" stop-color="#2f7a52"/><stop offset=".6" stop-color="#16472f"/><stop offset="1" stop-color="#0b2a1b"/></radialGradient>
   <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f6e2a0"/><stop offset=".5" stop-color="#d6b15e"/><stop offset="1" stop-color="#9c7a2e"/></linearGradient>
  </defs>
  <rect width="600" height="600" fill="#fff"/>
  <circle cx="300" cy="300" r="296" fill="url(#gold)"/>
  <circle cx="300" cy="300" r="280" fill="url(#g)"/>
  <circle cx="300" cy="300" r="232" fill="none" stroke="url(#gold)" stroke-width="7"/>
  ${Array.from({ length: 24 }, (_, i) => { const a = i * 15 * Math.PI / 180; return `<ellipse cx="${300 + 256 * Math.cos(a)}" cy="${300 + 256 * Math.sin(a)}" rx="14" ry="6" fill="#4fa374" transform="rotate(${i * 15 + 90} ${300 + 256 * Math.cos(a)} ${300 + 256 * Math.sin(a)})"/>`; }).join('')}
  ${star8(300, 300, 150, 62, 'url(#gold)')}
  ${star8(300, 300, 88, 40, '#f8eab8')}
  <circle cx="300" cy="300" r="22" fill="#fff8de"/>
  <ellipse cx="220" cy="185" rx="90" ry="40" fill="#fff" opacity=".12" transform="rotate(-35 220 185)"/>
  </svg>`;
}
// ---------- 3. Filigrane « Flocon » (800×800, transparent, blanc) ----------
function wmFlocon() {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800" viewBox="0 0 800 800">
  ${flake(400, 400, 370, '#ffffff', 26)}
  <circle cx="400" cy="400" r="92" fill="none" stroke="#fff" stroke-width="14"/>
  ${star8(400, 400, 60, 24, '#fff')}
  </svg>`;
}
// ---------- 4. Filigrane « Chouette de Noël » (800×800, transparent) ----------
function santaHat(x, y, w, rot = -12) { // x,y = centre du bas du bonnet
  return `<g transform="translate(${x},${y}) rotate(${rot})">
   <path d="M ${-w / 2} 0 C ${-w * .35} ${-w * .55}, ${w * .1} ${-w * .85}, ${w * .62} ${-w * .62} C ${w * .4} ${-w * .5}, ${w * .38} ${-w * .25}, ${w / 2} 0 Z" fill="#c8323c"/>
   <path d="M ${-w * .2} ${-w * .35} C ${0} ${-w * .62}, ${w * .3} ${-w * .7}, ${w * .55} ${-w * .6}" stroke="#a82630" stroke-width="${w * .03}" fill="none"/>
   <rect x="${-w * .56}" y="${-w * .1}" width="${w * 1.12}" height="${w * .2}" rx="${w * .1}" fill="#fbf6ea"/>
   <circle cx="${w * .66}" cy="${-w * .6}" r="${w * .1}" fill="#fbf6ea"/></g>`;
}
function beanie(x, y, w) {
  const h = w * .55; let ribs = '';
  for (let i = -5; i <= 5; i++) ribs += `<line x1="${i * w / 11}" y1="${-h * .12}" x2="${i * w / 11}" y2="${h * .12}" stroke="#b9cfdc" stroke-width="${w * .025}"/>`;
  let pat = ''; for (let i = -3; i <= 3; i++) pat += `<path d="M ${i * w / 7 - w * .04} ${-h * .5} l ${w * .04} ${-w * .05} l ${w * .04} ${w * .05}" stroke="#ffffff" stroke-width="${w * .02}" fill="none"/>`;
  return `<g transform="translate(${x},${y})">
   <path d="M ${-w / 2} 0 C ${-w / 2} ${-h * 1.35}, ${w / 2} ${-h * 1.35}, ${w / 2} 0 Z" fill="#2f6f97"/>
   <path d="M ${-w * .44} ${-h * .3} C ${-w * .3} ${-h * .95}, ${w * .3} ${-h * .95}, ${w * .44} ${-h * .3}" fill="#3d86b3"/>
   ${pat}
   <rect x="${-w * .54}" y="${-h * .14}" width="${w * 1.08}" height="${h * .3}" rx="${h * .12}" fill="#e9f3f8"/>${ribs}
   <circle cx="0" cy="${-h * 1.05}" r="${w * .13}" fill="#f7fbfd"/><circle cx="${-w * .04}" cy="${-h * 1.1}" r="${w * .06}" fill="#fff"/></g>`;
}
function owlWithHat(hat, size, extra = '') { // owl 600x570 scaled
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 600 600">${extra}
   <image href="${OWL}" x="0" y="20" width="600" height="570"/>${hat}</svg>`;
}
function holly(x, y, s, rot = 0) { // brin de houx : 2 feuilles + 3 baies
  const leaf = (a) => `<path transform="rotate(${a})" d="M0 0 C ${s*.25} ${-s*.18}, ${s*.55} ${-s*.22}, ${s*1.0} ${-s*.05} C ${s*.82} ${s*.02}, ${s*.86} ${s*.12}, ${s*.7} ${s*.14} C ${s*.6} ${s*.24}, ${s*.45} ${s*.18}, ${s*.38} ${s*.26} C ${s*.28} ${s*.2}, ${s*.15} ${s*.22}, 0 0 Z" fill="#2fa35a" stroke="#1b7a3e" stroke-width="${s*.04}"/><path transform="rotate(${a})" d="M ${s*.05} 0 L ${s*.85} ${-s*.04}" stroke="#1b7a3e" stroke-width="${s*.03}"/>`;
  return `<g transform="translate(${x},${y}) rotate(${rot})">${leaf(-150)}${leaf(-30)}
   <circle cx="${-s*.1}" cy="${s*.05}" r="${s*.16}" fill="#e3263a"/><circle cx="${s*.14}" cy="${s*.06}" r="${s*.16}" fill="#e3263a"/><circle cx="${s*.02}" cy="${-s*.15}" r="${s*.16}" fill="#ff3348"/>
   <circle cx="${-s*.14}" cy="${s*.0}" r="${s*.05}" fill="#fff" opacity=".85"/><circle cx="${s*.1}" cy="${s*.01}" r="${s*.05}" fill="#fff" opacity=".85"/><circle cx="${-s*.02}" cy="${-s*.2}" r="${s*.05}" fill="#fff" opacity=".85"/></g>`;
}
function bigSantaHat(x, y, w, rot = -8) { // bonnet rouge vif à pointe tombante, bordure et pompon blancs
  return `<g transform="translate(${x},${y}) rotate(${rot})">
   <path d="M ${-w*.5} 0 C ${-w*.46} ${-w*.62}, ${w*.12} ${-w*.9}, ${w*.52} ${-w*.74} C ${w*.74} ${-w*.64}, ${w*.86} ${-w*.48}, ${w*.84} ${-w*.32} C ${w*.66} ${-w*.48}, ${w*.48} ${-w*.42}, ${w*.5} 0 Z" fill="url(#hatRed)"/>
   <path d="M ${-w*.18} ${-w*.48} C ${w*.04} ${-w*.74}, ${w*.36} ${-w*.78}, ${w*.6} ${-w*.62}" stroke="#ff7a82" stroke-width="${w*.035}" fill="none" stroke-linecap="round" opacity=".75"/>
   <rect x="${-w*.6}" y="${-w*.12}" width="${w*1.2}" height="${w*.24}" rx="${w*.12}" fill="#ffffff"/>
   <circle cx="${w*.84}" cy="${-w*.3}" r="${w*.13}" fill="#ffffff"/>
   ${holly(-w*.3, -w*.02, w*.24, -20)}</g>`;
}
function wmChouetteNoel() {
  let sp = ''; const r = rnd(11);
  const pts = [[110,250,26],[690,230,30],[650,560,22],[140,600,20],[400,95,18],[700,420,14],[95,430,14]];
  for (const [x,y,R] of pts) sp += star8(x, y, R, R*.32, '#ffd75e');
  return `<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800" viewBox="0 0 800 800">
   <defs>
    <radialGradient id="halo" cx="50%" cy="52%" r="50%"><stop offset="0" stop-color="#fff3c4" stop-opacity="1"/><stop offset=".55" stop-color="#ffd76a" stop-opacity=".85"/><stop offset="1" stop-color="#ffb43c" stop-opacity="0"/></radialGradient>
    <linearGradient id="hatRed" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff3b45"/><stop offset="1" stop-color="#c8101e"/></linearGradient>
    <filter id="bright"><feComponentTransfer><feFuncR type="linear" slope="1.05" intercept=".38"/><feFuncG type="linear" slope="1.15" intercept=".26"/><feFuncB type="linear" slope="1.1" intercept=".08"/></feComponentTransfer><feColorMatrix type="saturate" values="1.35"/></filter>
   </defs>
   <circle cx="400" cy="450" r="330" fill="url(#halo)" opacity=".55"/>
   ${sp}
   <g transform="translate(120,240) scale(.94)" filter="url(#bright)"><image href="${OWL}" x="0" y="0" width="600" height="570"/></g>
   <g transform="translate(120,240) scale(.94)"><circle cx="224" cy="147" r="30" fill="#1c1408"/><circle cx="366" cy="147" r="30" fill="#1c1408"/><circle cx="241" cy="129" r="11" fill="#fff"/><circle cx="381" cy="129" r="11" fill="#fff"/></g>
   <g transform="translate(120,240) scale(.94)">${bigSantaHat(292, 30, 300, -8)}
     <path d="M 168 236 C 240 272, 360 272, 432 236 L 440 268 C 362 306, 238 306, 160 268 Z" fill="#e3263a"/>
     <path d="M 176 254 C 246 286, 354 286, 424 254" stroke="#ffffff" stroke-width="7" fill="none" stroke-dasharray="14 12"/>
     <path d="M 372 278 L 392 372 L 430 364 L 410 272 Z" fill="#c8101e"/><path d="M 389 358 L 428 350" stroke="#fff" stroke-width="7"/>
   </g>
  </svg>`;
}
// ---------- 5. Avatar « Chouette au bonnet » (512×512) ----------
function avatarBonnet() {
  const r = rnd(7); let fl = '';
  for (let i = 0; i < 26; i++) fl += flake(r() * 600, r() * 600, 8 + r() * 14, '#ffffff', 2.2, `opacity="${(.25 + r() * .45).toFixed(2)}"`);
  return `<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 600 600">
   <defs><radialGradient id="bg" cx="50%" cy="40%" r="70%"><stop offset="0" stop-color="#3f7fa8"/><stop offset="1" stop-color="#0e2d46"/></radialGradient></defs>
   <rect width="600" height="600" fill="url(#bg)"/>${fl}
   <ellipse cx="300" cy="590" rx="330" ry="70" fill="#eef6fa"/>
   <g transform="translate(60,85) scale(.8)"><image href="${OWL}" x="0" y="0" width="600" height="570"/>${beanie(298, 70, 310)}</g>
   </svg>`;
}
// ---------- 6. Board « Nuit de Noël » (1920×1280) ----------
function boardNoel() {
  const r = rnd(42); let snow = '', stars = '';
  for (let i = 0; i < 260; i++) { const x = r() * 1920, y = r() * 1280, s = 1.5 + r() * 4.5; snow += `<circle cx="${x.toFixed(0)}" cy="${y.toFixed(0)}" r="${s.toFixed(1)}" fill="#fff" opacity="${(.25 + r() * .6).toFixed(2)}"/>`; }
  for (let i = 0; i < 46; i++) { const x = r() * 1920, y = r() * 1280; stars += flake(x, y, 10 + r() * 22, '#ffffff', 2.5, `opacity="${(.18 + r() * .35).toFixed(2)}"`); }
  let gold = ''; for (let i = 0; i < 70; i++) gold += star8(r() * 1920, r() * 1280, 4 + r() * 6, 1.6, '#e8c874');
  // guirlande de sapin (haut et bas)
  let gar = ''; const r2 = rnd(5);
  for (const yy of [40, 1240]) for (let x = -20; x < 1960; x += 26) {
    const a = (r2() - .5) * 50; gar += `<ellipse cx="${x}" cy="${yy + (r2() - .5) * 26}" rx="34" ry="9" fill="${r2() > .5 ? '#1f5a3c' : '#2d7a50'}" transform="rotate(${a} ${x} ${yy})"/>`;
  }
  let balls = ''; for (const yy of [40, 1240]) for (let x = 90; x < 1920; x += 180) balls += `<circle cx="${x}" cy="${yy}" r="13" fill="url(#ball)"/><circle cx="${x - 4}" cy="${yy - 4}" r="4" fill="#fff" opacity=".8"/>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1280" viewBox="0 0 1920 1280">
   <defs><radialGradient id="sky" cx="50%" cy="45%" r="75%"><stop offset="0" stop-color="#1d3f6e"/><stop offset=".6" stop-color="#0f2547"/><stop offset="1" stop-color="#070f22"/></radialGradient>
   <radialGradient id="ball" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#fbe9a8"/><stop offset="1" stop-color="#b58a2c"/></radialGradient>
   <pattern id="knit" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M0 20 L10 10 L20 20 L30 10 L40 20" stroke="#ffffff" stroke-opacity=".04" stroke-width="3" fill="none"/></pattern></defs>
   <rect width="1920" height="1280" fill="url(#sky)"/><rect width="1920" height="1280" fill="url(#knit)"/>
   ${snow}${stars}${gold}${gar}
   <rect x="6" y="6" width="1908" height="1268" fill="none" stroke="#d6b15e" stroke-width="6" rx="10"/>
   </svg>`;
}
// Couleurs
const TRI_GIVRE = { dark: '#2c5f7d', light: '#dcecf2' };
const TRI_NOEL = { dark: '#1d5638', light: '#d4a94a' };
const BG_NOEL = '#0b1a33';

// ---------- Plateau de démonstration (aperçu du preset) ----------
function mockBoard(W, H, o) {
  // o: {frameUrl, bg, tri:{dark,light}, myCk, oppCk, wmUrl, divider}
  const pad = W * .045, bar = W * .06, fx = pad, fy = pad, fw = W - 2 * pad, fh = H - 2 * pad;
  const half = (fw - bar) / 2, pw = half / 6, ph = fh * .42, divH = fh - 2 * ph;
  let s = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
   <image href="${o.frameUrl}" x="0" y="0" width="${W}" height="${H}" preserveAspectRatio="xMidYMid slice"/>
   <rect x="${fx}" y="${fy}" width="${half}" height="${fh}" fill="${o.bg}"/><rect x="${fx + half + bar}" y="${fy}" width="${half}" height="${fh}" fill="${o.bg}"/>`;
  const px = i => { // point 1..24 → x center (vu du blanc : 1-6 bas droite)
    if (i <= 6) return fx + half + bar + half - (i - .5) * pw;
    if (i <= 12) return fx + half - (i - 6 - .5) * pw;
    if (i <= 18) return fx + (i - 12 - .5) * pw;
    return fx + half + bar + (i - 18 - .5) * pw;
  };
  for (let i = 1; i <= 24; i++) {
    const x = px(i), top = i > 12, col = i % 2 ? o.tri.dark : o.tri.light;
    s += top ? `<polygon points="${x - pw / 2 + 2},${fy} ${x + pw / 2 - 2},${fy} ${x},${fy + ph}" fill="${col}"/>` : `<polygon points="${x - pw / 2 + 2},${fy + fh} ${x + pw / 2 - 2},${fy + fh} ${x},${fy + fh - ph}" fill="${col}"/>`;
  }
  // filigranes (34% largeur d'une moitié ~ comme le jeu : 34% / 70% du plateau entier)
  if (o.wmUrl) for (const cx of [W * .23, W * .77]) s += `<image href="${o.wmUrl}" x="${cx - W * .17}" y="${H * .15}" width="${W * .34}" height="${H * .7}" opacity="${o.wmOpacity ?? .18}" preserveAspectRatio="xMidYMid meet"/>`;
  s += `<rect x="${fx + half}" y="${fy}" width="${bar}" height="${fh}" fill="#00000055"/>`;
  s += `<text x="${fx + half / 2}" y="${fy + fh / 2 + 9}" text-anchor="middle" font-family="Brico" font-size="${W * .02}" fill="#f3e3b0">🎲 ${o.divider} 🎲</text>`;
  s += `<text x="${fx + half + bar + half / 2}" y="${fy + fh / 2 + 9}" text-anchor="middle" font-family="Brico" font-size="${W * .02}" fill="#f3e3b0">🎲 ${o.divider} 🎲</text>`;
  // position de départ : blanc 24:2, 13:5, 8:3, 6:5 ; noir 1:2, 12:5, 17:3, 19:5 (15 + 15)
  const W_ = { 24: 2, 13: 5, 8: 3, 6: 5 }, B_ = { 1: 2, 12: 5, 17: 3, 19: 5 }; const cr = pw * .44; const step = Math.min(2 * cr, (fh * .47 - 2 * cr) / 4);
  const put = (map, url) => { for (const [p, n] of Object.entries(map)) { const i = +p, top = i > 12; for (let k = 0; k < n; k++) { const cy = top ? fy + cr + k * step : fy + fh - cr - k * step; s += `<clipPath id="c${i}_${k}"><circle cx="${px(i)}" cy="${cy}" r="${cr}"/></clipPath><image href="${url}" x="${px(i) - cr}" y="${cy - cr}" width="${2 * cr}" height="${2 * cr}" clip-path="url(#c${i}_${k})"/>`; } } };
  put(W_, o.myCk); put(B_, o.oppCk);
  let wc = 0; for (const n of Object.values(W_)) wc += n; let bc = 0; for (const n of Object.values(B_)) bc += n; if (wc !== 15 || bc !== 15) throw new Error('15 pions !');
  return s + '</svg>';
}

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  const shot = async (svg, w, h, file, transparent = false) => {
    await p.setViewportSize({ width: w, height: h });
    await p.setContent(`<html><head><style>@font-face{font-family:Brico;src:url(${FONT})}html,body{margin:0;background:transparent}</style></head><body>${svg}</body></html>`);
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(150);
    await p.screenshot({ path: file, omitBackground: transparent, clip: { x: 0, y: 0, width: w, height: h } });
  };
  const sh = (f) => path.join(OUT, f);
  await shot(wmChouetteNoel(), 800, 800, sh('watermark_chouette_de_noel.png'), true);
  await shot(boardNoel(), 1920, 1280, sh('board_theme_nuit_de_noel.png'));
  const d = f => 'data:image/png;base64,' + fs.readFileSync(f).toString('base64');
  const base = { frameUrl: d(sh('board_theme_nuit_de_noel.png')), bg: BG_NOEL, tri: TRI_NOEL, myCk: d(path.join(CK,'checker_skin_pions_hiver.png')), oppCk: d(path.join(CK,'checker_skin_sapin.png')), wmUrl: d(sh('watermark_chouette_de_noel.png')), divider: 'Joyeuses fêtes' };
  await shot(mockBoard(1280, 720, { ...base, wmOpacity: .18 }), 1280, 720, sh('src/preset_1280.png'));
  for (const op of [.18, .35]) await shot(mockBoard(1600, 1000, { ...base, wmOpacity: op }), 1600, 1000, sh(`src/apercu_op${Math.round(op*100)}.png`));
  await b.close();
  console.log('ok');
})();

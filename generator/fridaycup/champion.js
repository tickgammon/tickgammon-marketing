// Visuel « Champion de la semaine » de la Friday Cup (1080×1080, FR/EN/ES).
// Usage : node generator/fridaycup/champion.js <édition> "<vainqueur>" "<finaliste>"
// Sortie : visuels/friday-cup/champion-<NN>-fr.png, -en.png, -es.png (à pousser sur GitHub ;
// lien public : https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/main/visuels/friday-cup/champion-<NN>-<langue>.png)
const fs = require('fs'), path = require('path');
let chromium; try { ({ chromium } = require('playwright')); } catch (e) { ({ chromium } = require('/opt/npm-tools/node_modules/playwright')); }
const [, , edition, winner, finalist] = process.argv;
if (!edition || !winner || !finalist) { console.error('usage: node champion.js <édition> "<vainqueur>" "<finaliste>"'); process.exit(1); }
const out = path.join(__dirname, '..', '..', 'visuels', 'friday-cup');
fs.mkdirSync(out, { recursive: true });
const nn = String(edition).padStart(2, '0');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const lang of ['fr', 'en', 'es']) {
    const p = await b.newPage({ viewport: { width: 1080, height: 1080 } });
    p.on('pageerror', e => console.error('JS', e.message));
    await p.addInitScript(d => { window.DATA = d; }, { lang, edition: String(edition), winner, finalist });
    await p.goto('file://' + path.join(__dirname, 'champion.html'));
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
    const file = path.join(out, `champion-${nn}-${lang}.png`);
    await p.screenshot({ path: file, type: 'png' });
    console.log(file);
    await p.close();
  }
  await b.close();
})();

const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch();
  for (const lg of ['fr','en','es']) { const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
    await p.goto('file://' + path.resolve(__dirname, 'programme.html') + '?lang=' + lg); await p.waitForTimeout(600);
    await p.screenshot({ path: path.resolve(__dirname, '../../visuels/lecons/programme-saison1-' + lg + '.png') }); await p.close(); }
  await b.close(); })();

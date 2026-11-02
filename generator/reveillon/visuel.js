// Visuel du tournoi du réveillon 2026 (1080×1080, FR/EN/ES) → visuels/reveillon/reveillon-2026-<lang>.jpg
const path=require('path'),fs=require('fs');
let chromium; try { ({ chromium } = require('playwright')); } catch (e) { ({ chromium } = require('/opt/npm-tools/node_modules/playwright')); }
const out=path.join(__dirname,'..','..','visuels','reveillon'); fs.mkdirSync(out,{recursive:true});
(async()=>{const b=await chromium.launch();
for(const lang of ['fr','en','es']){const p=await b.newPage({viewport:{width:1080,height:1080}});
p.on('pageerror',e=>console.error('JS',e.message));
await p.addInitScript(l=>{window.LANG=l},lang);
await p.goto('file://'+path.join(__dirname,'visuel.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const f=path.join(out,`reveillon-2026-${lang}.jpg`);await p.screenshot({path:f,type:'jpeg',quality:90});console.log(f);await p.close()}
await b.close()})();

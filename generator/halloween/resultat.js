// Visuel résultats « La Nuit de la Chouette » (31/10/2026), 1080×1080 FR/EN/ES → visuels/halloween/
const path=require('path'),fs=require('fs');let chromium;try{({chromium}=require('playwright'))}catch(e){({chromium}=require('/opt/npm-tools/node_modules/playwright'))}
const out=path.join(__dirname,'..','..','visuels','halloween');fs.mkdirSync(out,{recursive:true});
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const lang of ['fr','en','es']){const p=await b.newPage({viewport:{width:1080,height:1080}});p.on('pageerror',e=>console.error(e.message));
await p.addInitScript(d=>{window.DATA=d},{lang,w:'Iparburu',f:'basdan',t:'ushaka'});
await p.goto('file://'+path.join(__dirname,'resultat.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const f=path.join(out,`nuit-chouette-resultats-${lang}.png`);await p.screenshot({path:f});console.log(f);await p.close()}
await b.close()})();

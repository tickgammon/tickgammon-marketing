// 27/10/2026 — node render.js <partie> <de> <à> <dossier> [temps…] (images 1920×1080, 30 i/s, reprise possible)
const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const [part,from,to,out,...tt]=process.argv.slice(2);
(async()=>{const data=fs.readFileSync(`data_${part}.json`,'utf8');
 const src=fs.existsSync(`pres_${part}.html`)?`pres_${part}.html`:'pres.html';const html=fs.readFileSync(src,'utf8').replace('<script>\nconst $',`<script>window.DATA=${data};</script><script>\nconst $`);
 const f=`_${part}.html`;fs.writeFileSync(f,html);
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1.5});
 p.on('pageerror',e=>console.error('ERR',e.message));
 await p.goto('file://'+process.cwd()+'/'+f,{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(600);
 fs.mkdirSync(out,{recursive:true});
 if(tt.length){for(const t of tt.map(Number)){await p.evaluate(t=>render(t),t);await p.screenshot({path:`${out}/t${t.toFixed(1)}.png`});}}
 else{for(let i=+from;i<+to;i++){const fn=`${out}/f${String(i).padStart(5,'0')}.png`;if(fs.existsSync(fn))continue;await p.evaluate(t=>render(t),i/30);await p.screenshot({path:fn});}}
 await b.close();})();

const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
// node render.js lang from to outdir [times...]
const [lang,from,to,out,...tt]=process.argv.slice(2);
(async()=>{const data=fs.readFileSync(`timeline${lang==='fr'?'':'_'+lang}.json`,'utf8');
 let html=fs.readFileSync('lecon3.html','utf8').replace('<script>\nconst $',`<script>window.DATA=${data};window.LANG='${lang}';window.SUBS=${process.env.SUBS!=='0'};</script><script>\nconst $`);
 const f=`_l3.html`;fs.writeFileSync(f,html);
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1.5});
 p.on('pageerror',e=>console.error('ERR',e.message));
 await p.goto('file://'+process.cwd()+'/'+f,{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
 fs.mkdirSync(out,{recursive:true});
 const times=tt.length?tt.map(Number):null;
 if(times){for(const t of times){await p.evaluate(t=>render(t),t);await p.screenshot({path:`${out}/t${t.toFixed(1)}.jpg`,type:'jpeg',quality:85});}}
 else{for(let i=+from;i<+to;i++){if(fs.existsSync(`${out}/f${String(i).padStart(5,"0")}.jpg`))continue;await p.evaluate(t=>render(t),i/30);await p.screenshot({path:`${out}/f${String(i).padStart(5,'0')}.jpg`,type:'jpeg',quality:90});}}
 await b.close();})();

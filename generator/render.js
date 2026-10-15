// Usage : node render.js <sujet> <langue fr|en|es> <format vertical|portrait|carre|paysage> <dossier_images> [test]
const fs=require('fs'),path=require('path');
let chromium;try{({chromium}=require('playwright'));}catch(e){({chromium}=require('/opt/npm-tools/node_modules/playwright'));}
const LAYOUTS={
 vertical:{W:720,H:1280,dir:'column',vb:540,tf:84,sf:29,kf:21,gap:40,pad:48,padT:90,url:20,urlY:34},
 portrait:{W:720,H:900,dir:'column',vb:400,tf:64,sf:23,kf:17,gap:22,pad:40,padT:64,url:17,urlY:22},
 carre:{W:720,H:720,dir:'column',vb:300,tf:50,sf:19,kf:15,gap:12,pad:30,padT:48,url:15,urlY:14},
 paysage:{W:1280,H:720,dir:'row',vb:500,tf:72,sf:26,kf:19,gap:70,pad:80,padT:60,url:17,urlY:20}};
const [,,sid,lang,fmt,out,test]=process.argv;
const SUB=JSON.parse(fs.readFileSync(path.join(__dirname,'subjects.json'),'utf8')).find(s=>s.id===sid);
if(!SUB){console.error('sujet inconnu',sid);process.exit(1);}
const L=LAYOUTS[fmt];
(async()=>{
 let html=fs.readFileSync(path.join(__dirname,'template.html'),'utf8').replace('<script>\nLOGO_PLACEHOLDER',
  `<script>window.LY=${JSON.stringify(L)};window.SUB=${JSON.stringify(SUB)};window.LANG=${JSON.stringify(lang)};</script><script>\n`+fs.readFileSync(path.join(__dirname,'logo.js'),'utf8'));
 if(!html.includes('window.SUB')){console.error('injection ratée');process.exit(1);}
 const page=path.join(__dirname,`_p_${sid}_${lang}_${fmt}.html`);fs.writeFileSync(page,html);
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:L.W,height:L.H},deviceScaleFactor:1.5});
 p.on('pageerror',e=>console.error('JS',e.message));
 await p.goto('file://'+page);await p.waitForTimeout(1500);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
 fs.rmSync(out,{recursive:true,force:true});fs.mkdirSync(out,{recursive:true});
 const times=test?[2,5,8.3,11.5,14.7,17.5,22]:Array.from({length:750},(_,i)=>i/30);
 let i=0;for(const t of times){await p.evaluate(t=>render(t),t);await p.screenshot({path:`${out}/f${String(i++).padStart(4,'0')}.jpg`,type:'jpeg',quality:90});}
 await b.close();fs.unlinkSync(page);
})();

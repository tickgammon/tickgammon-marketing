// Usage : node render.js <launch|teaser|howto> <fr|en|es> <vertical|carre|paysage> <dossier_images> [t1,t2,... pour un test]
const fs=require('fs'),path=require('path');
let chromium;try{({chromium}=require('playwright'));}catch(e){({chromium}=require('/opt/npm-tools/node_modules/playwright'));}
const LAYOUTS={
 vertical:{W:720,H:1280,dir:'column',vbW:640,vbH:600,tf:74,sf:28,kf:20,gap:34,pad:40,padT:96,url:20,urlY:34},
 carre:{W:720,H:720,dir:'column',vbW:440,vbH:385,tf:44,sf:19,kf:14,gap:12,pad:28,padT:44,url:15,urlY:14},
 paysage:{W:1280,H:720,dir:'row',vbW:640,vbH:560,tf:62,sf:24,kf:17,gap:50,pad:60,padT:60,url:17,urlY:20}};
const [,,vid,lang,fmt,out,test]=process.argv;
const L=LAYOUTS[fmt];
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--allow-file-access-from-files']});
 const p=await b.newPage({viewport:{width:L.W,height:L.H},deviceScaleFactor:1.5});
 p.on('pageerror',e=>console.error('JS',e.message));
 await p.addInitScript(d=>{window.LY=d.L;window.LANG=d.lang;window.VID=d.vid;},{L,lang,vid});
 await p.goto('file://'+path.join(__dirname,'ff.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
 const END=await p.evaluate(()=>window.END);
 fs.rmSync(out,{recursive:true,force:true});fs.mkdirSync(out,{recursive:true});
 const times=test?test.split(',').map(Number):Array.from({length:Math.round(END*30)},(_,i)=>i/30);
 let i=0;for(const t of times){await p.evaluate(t=>render(t),t);await p.screenshot({path:`${out}/f${String(i++).padStart(4,'0')}.jpg`,type:'jpeg',quality:90});}
 await b.close();console.log(vid,lang,fmt,END,times.length);
})();

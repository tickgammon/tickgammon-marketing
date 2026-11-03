// Usage : node render.js <galette|soldes|tournoi> <fr|en|es> <dossier_images> [t1,t2,... pour un test]
const fs=require('fs'),path=require('path');
let chromium;try{({chromium}=require('playwright'));}catch(e){({chromium}=require('/opt/npm-tools/node_modules/playwright'));}
const [,,vid,lang,out,test]=process.argv;
const L={W:720,H:1280};
(async()=>{
 const b=await chromium.launch({args:['--allow-file-access-from-files']});
 const p=await b.newPage({viewport:{width:L.W,height:L.H},deviceScaleFactor:1.5});
 p.on('pageerror',e=>console.error('JS',e.message));
 await p.addInitScript(d=>{window.LY=d.L;window.LANG=d.lang;window.VID=d.vid;},{L,lang,vid});
 await p.goto('file://'+path.join(__dirname,'jan.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
 const END=await p.evaluate(()=>window.END);
 fs.rmSync(out,{recursive:true,force:true});fs.mkdirSync(out,{recursive:true});
 const times=test?test.split(',').map(Number):Array.from({length:Math.round(END*30)},(_,i)=>i/30);
 let i=0;for(const t of times){await p.evaluate(t=>render(t),t);await p.screenshot({path:`${out}/f${String(i++).padStart(4,'0')}.jpg`,type:'jpeg',quality:90});}
 await b.close();console.log(vid,lang,END,times.length);
})();

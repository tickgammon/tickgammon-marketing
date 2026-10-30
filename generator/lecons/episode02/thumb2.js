// Miniature YouTube leçon 2 (1280×720) : réutilise lecon2.html (scène 3-1) + titre
const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const L=process.argv[2]||'fr';const TX={fr:['Leçon 2','Les','ouvertures','15 coups à connaître'],en:['Lesson 2','The','openings','15 moves to know'],es:['Lección 2','Las','aperturas','15 jugadas que conocer']}[L];
(async()=>{const data=fs.readFileSync('timeline.json','utf8');const D=JSON.parse(data);const P11=D.tl.find(x=>x.p==='P11');
 let html=fs.readFileSync('lecon2.html','utf8').replace('<script>\nconst $',`<script>window.DATA=${data};window.LANG='fr';</script><script>\nconst $`);
 fs.writeFileSync('_th.html',html);const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
 await p.goto('file://'+process.cwd()+'/_th.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
 await p.evaluate(([t,TX])=>{render(t);
  document.querySelector('#top').style.opacity=0;document.querySelector('#prog').style.display='none';
  const bd=document.querySelector('#board');bd.style.left='470px';bd.style.top='210px';bd.style.transform='scale(1.05) rotate(-4deg)';bd.style.filter='drop-shadow(0 30px 40px rgba(0,0,0,.5))';
  const ow=document.querySelector('#owlw');ow.style.left='-20px';ow.style.top='330px';ow.style.zIndex=6;document.querySelector('#owl').style.transform='scale(1.05)';
  document.querySelector('#eyeR').style.opacity=1;document.querySelector('#eyeL').style.opacity=0;
  document.querySelector('#ov').innerHTML=`
  <div class="a" style="left:56px;top:40px;z-index:7"><span class="pill" style="font-size:22px;padding:8px 22px">${TX[0]}</span>
   <div class="big" style="font-size:118px;margin-top:14px;line-height:.9;text-shadow:0 8px 0 rgba(0,0,0,.35)">${TX[1]}<br><span style="color:#f6d77a">${TX[2]}</span></div></div>
  <div class="a card" style="left:860px;top:40px;padding:18px 26px;transform:rotate(5deg);z-index:7;display:flex;gap:14px;align-items:center;background:#0f4030;border:4px solid #c9a86a">${dieSvg(3,'#fdfbf0',96)}${dieSvg(1,'#ff7a59',96)}</div>
  <div class="a" style="left:300px;top:345px;z-index:7;transform:rotate(-6deg)"><span class="bf" style="display:inline-block;background:#fdfbf0;color:#0d3326;font-size:46px;border-radius:20px;padding:10px 24px;box-shadow:0 10px 0 rgba(0,0,0,.3)">${TX[3]}</span></div>`;
 },[P11.t0+P11.d-0.2,TX]);
 await p.screenshot({path:`miniature_lecon2_ouvertures${L==='fr'?'':'_'+L}.jpg`,type:'jpeg',quality:92});await b.close();})();

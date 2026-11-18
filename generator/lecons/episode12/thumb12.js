// Miniature YouTube leçon 12 (1280×720) : scène P10 (prime complet) + titre
const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');const {execSync}=require('child_process');
const L=process.argv[2]||'fr';const TX={fr:['Leçon 12','Parlez','backgammon !','Blot, prime, gammon…'],en:['Lesson 12','Talk','backgammon!','Blot, prime, gammon…'],es:['Lección 12','¡Habla','backgammon!','Blot, prime, gammon…']}[L];
(async()=>{const data=fs.readFileSync('timeline.json','utf8');const D=JSON.parse(data);const P=D.tl.find(x=>x.p==='P10');
 let html=fs.readFileSync('lecon12.html','utf8').replace('<script>\nconst $',`<script>window.DATA=${data};window.LANG='fr';</script><script>\nconst $`);
 fs.writeFileSync('_th.html',html);const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
 await p.goto('file://'+process.cwd()+'/_th.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
 await p.evaluate(([t,TX])=>{render(t);
  document.querySelector('#top').style.opacity=0;document.querySelector('#prog').style.display='none';
  const sub=document.querySelector('#sub');if(sub)sub.style.display='none';
  const ov=document.querySelector('#ov');ov.querySelectorAll('.card').forEach(e=>{if(e.getBoundingClientRect().left>800)e.remove();});
  ov.style.transform='translate(-60px,40px) scale(.95) rotate(-3deg)';ov.style.transformOrigin='0 0';
  const bd=document.querySelector('#board');if(bd)bd.style.transformOrigin='0 50%';bd.style.transform='translate(-14px,20px) scale(.84) rotate(-2deg)';const ow=document.querySelector('#owlw');if(ow){ow.style.left='1010px';ow.style.top='400px';ow.style.zIndex=6;}
  const t2=document.createElement('div');t2.style.cssText='position:absolute;inset:0;z-index:9';
  t2.innerHTML=`<div class="a" style="left:690px;top:34px"><span class="pill" style="font-size:24px;padding:8px 22px">${TX[0]}</span>
   <div class="big" style="font-size:${Math.min(70,Math.floor(560/(Math.max(TX[1].length,TX[2].length)*0.66)))}px;margin-top:14px;line-height:.98;white-space:nowrap;text-shadow:0 10px 0 rgba(0,0,0,.35)">${TX[1]}<br><span style="color:#f6d77a">${TX[2]}</span></div></div>
  <div class="a" style="left:560px;top:560px;transform:rotate(-4deg)"><span class="bf" style="display:inline-block;background:#fdfbf0;color:#0d3326;font-size:${TX[3].length>18?40:46}px;border-radius:20px;padding:10px 24px;box-shadow:0 12px 0 rgba(0,0,0,.3)">${TX[3]}</span></div>`;
  document.querySelector('#ov').parentElement.appendChild(t2);
 },[P.t0+P.d*.95,TX]);
 await p.screenshot({path:'_th.png'});await b.close();
 execSync(`ffmpeg -loglevel error -y -i _th.png -vf scale=1280:720 -q:v 2 miniature_lecon12_vocabulaire${L==='fr'?'':'_'+L}.jpg`);})();

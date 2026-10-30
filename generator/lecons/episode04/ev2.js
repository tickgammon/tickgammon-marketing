const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
(async()=>{const data=fs.readFileSync('timeline.json','utf8');const D=JSON.parse(data);
 let html=fs.readFileSync('lecon4.html','utf8').replace('<script>\nconst $',`<script>window.DATA=${data};window.LANG='fr';</script><script>\nconst $`);
 fs.writeFileSync('_ev.html',html);const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1280,height:720}});
 p.on('pageerror',e=>console.error('ERR',e.message));await p.goto('file://'+process.cwd()+'/_ev.html');
 const ev=await p.evaluate(T=>{for(let t=0;t<T;t+=1/15)render(t);return Object.keys(window.EVT);},D.total);
 fs.writeFileSync('evt_raw.json',JSON.stringify(ev));await b.close();console.log(ev.length);})();

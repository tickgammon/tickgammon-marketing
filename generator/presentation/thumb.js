// 28/10/2026 — node thumb.js <sortie.jpg> : capture la miniature YouTube (1280×720)
const { chromium } = require('/opt/npm-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1280,height:720}});
 await p.goto('file://'+process.cwd()+'/thumb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
 await p.screenshot({path:process.argv[2],type:'jpeg',quality:92});await b.close();})();

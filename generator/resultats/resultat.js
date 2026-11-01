// Visuel « Résultats » d'un tournoi officiel TickGammon (01/11/2026), 1080×1080, FR/EN/ES, PNG + JPEG (TikTok).
// Usage : node generator/resultats/resultat.js <fichier.json>
//   JSON : {"id":64,"name":"La Nuit de la Chouette","theme":"felt|halloween|noel","total":5000,
//           "podium":[{"name":"Iparburu","tgc":2500},{"name":"basdan","tgc":1500},{"name":"ushaka","tgc":250}]}
// Sortie : visuels/resultats/resultats-<id>-<fr|en|es>.png et .jpg
// Lien public : https://raw.githubusercontent.com/tickgammon/tickgammon-marketing/main/visuels/resultats/resultats-<id>-<langue>.<png|jpg>
const path=require('path'),fs=require('fs');let chromium;try{({chromium}=require('playwright'))}catch(e){({chromium}=require('/opt/npm-tools/node_modules/playwright'))}
const D=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const out=path.join(__dirname,'..','..','visuels','resultats');fs.mkdirSync(out,{recursive:true});
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const lang of ['fr','en','es']){const p=await b.newPage({viewport:{width:1080,height:1080}});p.on('pageerror',e=>console.error(e.message));
await p.addInitScript(d=>{window.DATA=d},Object.assign({},D,{lang}));
await p.goto('file://'+path.join(__dirname,'resultat.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const f=path.join(out,`resultats-${D.id}-${lang}`);await p.screenshot({path:f+'.png'});await p.screenshot({path:f+'.jpg',type:'jpeg',quality:92});console.log(f+'.png / .jpg');await p.close()}
await b.close()})();

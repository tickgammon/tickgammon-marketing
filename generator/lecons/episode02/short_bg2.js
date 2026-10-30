const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 2 · Les ouvertures',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Pourquoi 15 ouvertures ?','Lire un coup','Faire un point','Le 6-1 et le bar point','Courir avec un 6','Préparer : les constructeurs','Répondre avec un double','Les pièges à éviter']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 2 · The openings',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','Why 15 openings?','Reading a move','Making a point','6-1 and the bar point','Running with a 6','Building: the builders','Replying with a double','Traps to avoid']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 2 · Las aperturas',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','¿Por qué 15 aperturas?','Leer una jugada','Hacer un punto','El 6-1 y el bar point','Correr con un 6','Preparar: los constructores','Responder con un doble','Trampas que evitar']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts2',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts2/bg_${L}_${c}.png`});}
 await b.close();})();

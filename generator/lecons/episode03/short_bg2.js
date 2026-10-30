const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 3 · Le videau',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Le videau, c\'est quoi ?','Comment ça marche','Le videau multiplie tout','La règle des 25 %','Quand doubler ?','Les situations typiques','Les règles spéciales','Les erreurs à éviter']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 3 · The doubling cube',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','What is the doubling cube?','How it works','The cube multiplies everything','The 25% rule','When to double?','Typical situations','Special rules','Mistakes to avoid']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 3 · El cubo doblador',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','¿Qué es el cubo doblador?','Cómo funciona','El cubo lo multiplica todo','La regla del 25 %','¿Cuándo doblar?','Situaciones típicas','Reglas especiales','Errores que evitar']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts2',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts2/bg_${L}_${c}.png`});}
 await b.close();})();

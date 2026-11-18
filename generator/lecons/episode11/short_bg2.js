const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 11 · L\'histoire du backgammon',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Les lointains ancêtres','Rome : la tabula','La Perse et le nard','Le Moyen Âge','Le nom « backgammon »','Le videau et l\'âge d\'or','Les ordinateurs','Aujourd\'hui : en ligne']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 11 · The history of backgammon',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','Distant ancestors','Rome: tabula','Persia and nard','The Middle Ages','The name “backgammon”','The cube and the golden age','Computers','Today: online']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 11 · La historia del backgammon',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','Los lejanos antepasados','Roma: la tabula','Persia y el nard','La Edad Media','El nombre «backgammon»','El cubo y la edad de oro','Los ordenadores','Hoy: en línea']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts2',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts2/bg_${L}_${c}.png`});}
 await b.close();})();

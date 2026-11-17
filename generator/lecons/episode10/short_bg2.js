const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 10 · Jacquet, trictrac et backgammon',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Une seule famille','Le même matériel','Le backgammon','Le jacquet : le départ','Le jacquet : bloquer','Le trictrac','Le mot « trictrac »','En résumé']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 10 · Jacquet, trictrac and backgammon',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','One family','The same equipment','Backgammon','Jacquet: the start','Jacquet: blocking','Trictrac','The word “trictrac”','In short']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 10 · Jacquet, trictrac y backgammon',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','Una sola familia','El mismo material','El backgammon','El jacquet: la salida','El jacquet: bloquear','El trictrac','La palabra «trictrac»','En resumen']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts2',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts2/bg_${L}_${c}.png`});}
 await b.close();})();

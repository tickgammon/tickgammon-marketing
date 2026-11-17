const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 8 · Jouer en ligne',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Jouer en ligne','Formats et rythmes','L\'ELO','Comment l\'ELO bouge','L\'expérience','Le classement','Quatre conseils','Le videau en ligne']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 8 · Playing online',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','Playing online','Formats and speeds','ELO','How ELO moves','Experience','The ranking','Four tips','The cube online']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 8 · Jugar en línea',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','Jugar en línea','Formatos y ritmos','El ELO','Cómo se mueve el ELO','La experiencia','La clasificación','Cuatro consejos','El cubo en línea']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts2',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts2/bg_${L}_${c}.png`});}
 await b.close();})();

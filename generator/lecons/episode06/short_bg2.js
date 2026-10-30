const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 6 · La chouette',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Le principe','Les trois rôles','Le tirage','Les places tournent','Les points','Un videau chacun','Pourquoi on aime','Conseils']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 6 · The chouette',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','The idea','The three roles','The draw','Rotating places','The points','A cube each','Why we love it','Tips']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 6 · La chouette',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','La idea','Los tres papeles','El sorteo','Los puestos giran','Los puntos','Un cubo para cada uno','Por qué gusta','Consejos']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts2',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts2/bg_${L}_${c}.png`});}
 await b.close();})();

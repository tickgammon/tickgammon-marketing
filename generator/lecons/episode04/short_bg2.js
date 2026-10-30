const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 4 · La course',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Qu\'est-ce qu\'une course ?','Compter les pips','Qui mène ?','Ramener ses pions','Ne pas gaspiller','La sortie sans contact','La sortie avec contact','Videau et gammon']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 4 · The race',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','What is a race?','Counting pips','Who is ahead?','Bringing checkers home','Don\'t waste pips','Bearing off, no contact','Bearing off with contact','Cube and gammon']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 4 · La carrera',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','¿Qué es una carrera?','Contar los pips','¿Quién va por delante?','Llevar las fichas a casa','No desperdiciar','La salida sin contacto','La salida con contacto','Cubo y gammon']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts2',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts2/bg_${L}_${c}.png`});}
 await b.close();})();

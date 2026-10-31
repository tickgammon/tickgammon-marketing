const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 7 · Contre l\'ordinateur',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Pourquoi l\'ordinateur','GNU Backgammon','Les dés sont honnêtes','L\'analyse','Résultat ≠ jeu','L\'Entraînement','La méthode','Pour débuter']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 7 · Against the computer',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','Why the computer','GNU Backgammon','Honest dice','The analysis','Result ≠ play','Training','The method','Getting started']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 7 · Contra el ordenador',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','Por qué el ordenador','GNU Backgammon','Dados honestos','El análisis','Resultado ≠ juego','Entrenamiento','El método','Para empezar']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts2',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts2/bg_${L}_${c}.png`});}
 await b.close();})();

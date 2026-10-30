const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 5 · Les probabilités',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Les 36 combinaisons','Les lancers précis','Au moins un chiffre','Le tir direct','Le tir indirect','Rentrer depuis la barre','Trois réflexes','Les dés et le videau']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 5 · Dice probabilities',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','The 36 combinations','Specific rolls','At least one number','The direct shot','The indirect shot','Coming in from the bar','Three reflexes','Dice and the cube']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 5 · Las probabilidades',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','Las 36 combinaciones','Las tiradas concretas','Al menos un número','El tiro directo','El tiro indirecto','Entrar desde la barra','Tres reflejos','Los dados y el cubo']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts2',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts2/bg_${L}_${c}.png`});}
 await b.close();})();

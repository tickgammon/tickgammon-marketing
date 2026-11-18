const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 12 · Le vocabulaire du joueur',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Le plateau','Blot, point et ancre','Bloquer','Frapper et rentrer','La course','Le videau','Gammon et backgammon','Match et chouette']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 12 · The player\'s vocabulary',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','The board','Blot, point and anchor','Blocking','Hitting and entering','The race','The doubling cube','Gammon and backgammon','Matches and chouette']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 12 · El vocabulario del jugador',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','El tablero','Blot, punto y ancla','Bloquear','Golpear y entrar','La carrera','El cubo doblador','Gammon y backgammon','Match y chouette']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts2',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts2/bg_${L}_${c}.png`});}
 await b.close();})();

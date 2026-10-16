const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 1 · Les règles',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Le but du jeu','Le plateau et le matériel','La position de départ','Lancer les dés et déplacer ses pions','Frapper un pion et la barre','Sortir ses pions','Simple, gammon, backgammon','Le videau et la règle de Crawford']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 1 · The rules',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','The goal of the game','The board and the equipment','The starting position','Rolling the dice and moving','Hitting and the bar','Bearing off','Single, gammon, backgammon','The doubling cube and the Crawford rule']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 1 · Las reglas',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','El objetivo del juego','El tablero y el material','La posición inicial','Tirar los dados y mover','Golpear una ficha y la barra','Sacar las fichas','Simple, gammon, backgammon','El cubo doblador y la regla Crawford']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts/bg_${L}_${c}.png`});}
 await b.close();})();

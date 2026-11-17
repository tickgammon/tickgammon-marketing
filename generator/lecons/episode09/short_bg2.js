const { chromium } = require('/opt/npm-tools/node_modules/playwright');const fs=require('fs');
const C={fr:{series:'LES LEÇONS DE LA CHOUETTE',ep:'Épisode 9 · Tournois, clubs et cours',chapw:'Chapitre',full:'La leçon complète sur YouTube',free:'Jouez gratuitement en ligne',
 chap:['','Jouer à plusieurs','Créer un tournoi','Les trois formats','Le jour du tournoi','Clubs et clans','La vie du club','Les cours','Cours particuliers']},
 en:{series:"THE OWL'S LESSONS",ep:'Episode 9 · Tournaments, clubs and lessons',chapw:'Chapter',full:'Full lesson on YouTube',free:'Play for free online',
 chap:['','Playing with others','Creating a tournament','The three formats','Tournament day','Clubs and clans','Club life','Lessons','Private lessons']},
 es:{series:'LAS LECCIONES DE LA LECHUZA',ep:'Episodio 9 · Torneos, clubes y clases',chapw:'Capítulo',full:'La lección completa en YouTube',free:'Juega gratis en línea',
 chap:['','Jugar en compañía','Crear un torneo','Los tres formatos','El día del torneo','Clubes y clanes','La vida del club','Las clases','Clases particulares']}};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1080,height:1920}});
 fs.mkdirSync('shorts2',{recursive:true});
 for(const L of ['fr','en','es'])for(let c=1;c<=8;c++){const S=C[L];const P={series:S.series,ep:S.ep,chap:`${S.chapw} ${c}`,title:S.chap[c],full:S.full,free:S.free};
  const h=fs.readFileSync('short_bg.html','utf8').replace('<script>',`<script>window.P=${JSON.stringify(P)};</script><script>`);fs.writeFileSync('_sb.html',h);
  await p.goto('file://'+process.cwd()+'/_sb.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
  await p.screenshot({path:`shorts2/bg_${L}_${c}.png`});}
 await b.close();})();

// Aperçu du Plateau de Noël (texte « Joyeuses fêtes ») pour les vidéos de décembre
const fs=require('fs'),path=require('path');
let chromium;try{({chromium}=require('playwright'));}catch(e){({chromium}=require('/opt/npm-tools/node_modules/playwright'));}
const SRC='/home/claude/work/decembre/cosmetiques/src/gen.js';
const g=fs.readFileSync(SRC,'utf8');
const fn=g.slice(g.indexOf('function mockBoard'),g.indexOf('(async () =>'));
eval(fn.replace('function mockBoard','global.mockBoard=function'));
const FONT='data:font/woff2;base64,'+fs.readFileSync('/home/claude/tickgammon-marketing/generator/lecons/brico800.woff2').toString('base64');
const C='/home/claude/work/decembre/cosmetiques/apercus_png/';
const d=f=>'data:image/png;base64,'+fs.readFileSync(C+f).toString('base64');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
 const svg=mockBoard(1280,720,{frameUrl:d('board_theme_nuit_de_noel.png'),bg:'#0b1a33',tri:{dark:'#1d5638',light:'#d4a94a'},myCk:d('checker_skin_pions_hiver.png'),oppCk:d('checker_skin_sapin.png'),wmUrl:d('watermark_chouette_de_noel.png'),divider:'Joyeuses fêtes'});
 await p.setContent(`<html><head><style>@font-face{font-family:Brico;src:url(${FONT})}html,body{margin:0}</style></head><body>${svg}</body></html>`);
 await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);
 await p.screenshot({path:path.join(__dirname,'img/plateau_noel.png')});await b.close();})();

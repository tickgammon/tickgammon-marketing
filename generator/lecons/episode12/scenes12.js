// ---- Leçon 12 : le vocabulaire du joueur
// mots (FR + EN + ES) en carte
const WORD=(fr,en,es,fs=46,bg='#fdfbf0')=>`<div class="card" style="padding:14px 30px;text-align:center;background:${bg}">${NAME(fr,en,es,fs)}</div>`;
// états de plateau (toujours 15 pions par couleur)
function blotState(){const s=startState();s.p[W(13)]-=1;s.p[W(9)]+=1;return s;}           // blot blanc sur le 9
function primeState(){const s=newState();[4,5,6,7,8,9].forEach(n=>s.p[W(n)]=2);s.p[W(13)]=3;s.p[B(24)]=-2;s.p[B(13)]=-5;s.p[B(8)]=-4;s.p[B(6)]=-4;return s;}
function hitState(){const s=startState();s.p[B(24)]+=1;s.p[W(5)]=-1;return s;}             // blot noir sur notre point 5
function afterHit(){const s=startState();s.p[B(24)]+=1;s.p[W(13)]-=1;s.p[W(5)]=1;s.barB=1;return s;}
function raceState(){const s=newState();[2,2,3,3,2,2].forEach((n,k)=>s.p[W(k+1)]=n);s.p[W(8)]=1;[3,3,2,2,2,2].forEach((n,k)=>s.p[B(k+1)]=-n);s.p[B(9)]=-1;return s;}
function homeState(){const s=newState();[3,3,3,2,2,2].forEach((n,k)=>s.p[W(k+1)]=n);[3,3,3,2,2,2].forEach((n,k)=>s.p[B(k+1)]=-n);return s;}
function gammonState(){const s=newState();s.offW=15;[3,3,3,3,3].forEach((n,k)=>s.p[B(8+k)]=-n);return s;}
function bgState(){const s=newState();s.offW=15;s.barB=1;s.p[W(3)]=-1;[3,3,3,3,1].forEach((n,k)=>s.p[B(8+k)]=-n);return s;}
const RACE_W=`M${cx(W(8))} ${yB-70} L${cx(W(1))} ${yB-70} L${TRX+26} ${yB-70}`;
const RACE_B=`M${cx(B(9))} ${yT+70} L${cx(B(1))} ${yT+70} L${TRX+26} ${yT+70}`;
const SCORE=(a,b,to,hi)=>`<div class="card" style="padding:14px 26px;display:flex;gap:18px;align-items:center;background:#0f4030;color:#fdfbf0;border:3px solid #c9a86a">${av('A',70,{name:false})}<span class="bf" style="font-size:64px;color:${hi===0?'#f6d77a':'#fdfbf0'}">${a}</span><span class="bf" style="font-size:40px;color:#c9a86a">–</span><span class="bf" style="font-size:64px;color:${hi===1?'#f6d77a':'#fdfbf0'}">${b}</span>${av('C',70,{name:false})}<span class="pill" style="font-size:22px;margin-left:8px">/ ${to}</span></div>`;
function lessonGrid(lt,a){let h='<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:14px">';for(let k=1;k<=12;k++){const p=pop(lt,a+k*.12,.3);h+=`<div style="position:relative;${sc(p)}"><div class="card bf" style="width:92px;height:92px;display:flex;align-items:center;justify-content:center;font-size:40px;background:${k===12?'#f6d77a':'#fdfbf0'}">${k}</div><div class="a" style="right:-10px;top:-12px">${ck(38)}</div></div>`;}return h+'</div>';}

const SC={
 P01(lt,D,X){X.board=null;X.top=0;X.owl={x:150+(1-eo(seg(lt,0,1.3)))*1000,y:150-Math.sin(seg(lt,0,1.3)*Math.PI)*90,s:1.35,wave:[1.2,4.2],wink:[5.2,5.6]};X.owlFront=1;X.conf=lt;
  X.ov=`<div class="a" style="left:640px;top:130px;width:600px;opacity:${eo(seg(lt,1,1.6))};transform:translateX(${(1-eo(seg(lt,1,1.6)))*40}px)">
  <div class="pill">TickGammon</div>
  <div class="big" style="font-size:66px;margin-top:14px">Les leçons<br>de la <span style="color:#c9a86a">chouette</span></div>
  <div style="font-size:23px;font-weight:800;color:#c9a86a;margin-top:12px">The Owl's Lessons · Las lecciones de la lechuza</div>
  <div style="margin-top:30px;display:flex;gap:18px;align-items:center;opacity:${eo(seg(lt,2,2.6))};transform:translateY(${(1-eo(seg(lt,2,2.6)))*20}px)">
   <div style="transform:rotate(${Math.sin(lt*3)*6}deg)">${BOOK(90,'#7fd3ff')}</div>
   <div><span class="pill" style="background:#fdfbf0">12</span><div class="bf" style="font-size:34px;margin-top:8px;line-height:1.05">Le vocabulaire du joueur</div><div style="font-size:20px;font-weight:800;color:#d9e6dc;margin-top:6px">The player's vocabulary · El vocabulario del jugador</div></div></div></div>`;},
 P02(lt,D,X){X.board=null;const w=[['Blot','#fdfbf0'],['Prime','#7fe0a0'],['Gammon','#ff7a59'],[cubeSvg(64,70),'#f6d77a']];const t0=D*.15,st=D*.12;
  X.ov=`<div class="a" style="left:60px;top:170px;width:740px;display:grid;grid-template-columns:1fr 1fr;gap:22px">${w.map((x,k)=>`<div class="card bf" style="height:150px;display:flex;align-items:center;justify-content:center;font-size:52px;background:${x[1]};${sc(pop(lt,t0+k*st))}">${x[0]}</div>`).join('')}</div>`+at(430,610,`<div style="display:flex;gap:14px;align-items:center">${BOOK(80,'#7fd3ff')}${ck(60)}</div>`,pop(lt,D*.7));},
 // 1. le plateau
 P03(lt,D,X){X.board={st:startState(),labels:{n:seg(lt,D*.2,D*.85)*24},hl:[{i:W(6),al:eo(seg(lt,.2,.6))}]};X.ov=rcard(NAME('Point','Point','Punto',46),pop(lt,.3))+rcard(`<span class="bf" style="font-size:72px;color:#f6d77a">24</span>`,pop(lt,D*.8),410,300);},
 P04(lt,D,X){const a=D*.4;X.board={st:startState(),labels:{n:24,al:.8},mv:[M(13,8,a,a+1.2)],paths:[arcI(W(13),W(8),110,'#f6d77a',eo(seg(lt,a-.6,a)))],marks:[{k:'tag',x:(cx(W(13))+cx(W(8)))/2,y:yT+200,t:'5',al:seg(lt,a+1.2,a+1.5),bg:'#f6d77a'}]};
  X.ov=rcard(`<div class="bf" style="font-size:46px">Pip</div><div style="display:flex;gap:10px;justify-content:center;margin-top:10px">${[0,1,2,3,4].map(k=>`<div style="${sc(pop(lt,a+k*.22))}">${mini('w',44)}</div>`).join('')}</div><div class="bf" style="font-size:40px;color:#f6d77a;margin-top:8px;opacity:${eo(seg(lt,a+1.2,a+1.5))}">5 = 5</div>`,pop(lt,.2));},
 P05(lt,D,X){const a=D*.4,b=D*.65;X.board={st:startState(),barHl:Math.sin(Math.PI*seg(lt,.2,a))*1,zones:[{a:W(6),b:W(1),al:eo(seg(lt,a,a+.4))*.8,c:'#7fe0a0'},{a:W(12),b:W(7),al:eo(seg(lt,b,b+.4))*.8,c:'#7fd3ff'}],labels:{n:24,al:.7}};
  X.ov=rcard(`<div style="display:flex;flex-direction:column;gap:10px;align-items:center"><div class="bf" style="font-size:30px">Barre · Bar · Barra</div><div style="opacity:${eo(seg(lt,a,a+.4))};font-weight:800;font-size:24px;color:#7fe0a0">1 → 6 : Jan intérieur<br><span style="font-size:17px;color:#c9a86a">Home board · Cuadrante interior</span></div><div style="opacity:${eo(seg(lt,b,b+.4))};font-weight:800;font-size:24px;color:#7fd3ff">7 → 12 : Jan extérieur<br><span style="font-size:17px;color:#c9a86a">Outer board · Cuadrante exterior</span></div></div>`,pop(lt,.2));},
 // 2. blot, point, ancre
 P06(lt,D,X){const a=D*.45;X.board={st:blotState(),marks:[{k:'target',x:cx(W(9)),y:yB,al:eo(seg(lt,a,a+.3))},{k:'tag',x:cx(W(9)),y:yB-90,t:'BLOT',al:seg(lt,.3,.6),bg:'#ff7a59'}]};
  X.ov=rcard(`<div class="bf" style="font-size:52px">Blot</div><div style="display:flex;gap:12px;justify-content:center;margin-top:10px">${mini('w',60)}<span class="bf" style="font-size:44px;color:#c9a86a">=</span><span class="bf" style="font-size:52px;color:#ff7a59">1</span></div>`,pop(lt,.2));},
 P07(lt,D,X){const a=D*.25;X.board={st:startState(),mv:[M(8,5,a,a+.8),M(6,5,a+.3,a+1.1)],marks:[{k:'lock',x:cx(W(5)),y:yB-110,al:seg(lt,a+1.2,a+1.5)}],hl:[{i:W(5),al:eo(seg(lt,a+1.1,a+1.4)),c:'#7fe0a0'}]};note(X,lt,'8/5 6/5',[3,1],.1);},
 P08(lt,D,X){const a=D*.25,b=D*.6;X.board={st:startState(),mv:[M(24,20,a,a+.8),M(24,20,a+.3,a+1.1)],zones:[{a:W(24),b:W(19),al:eo(seg(lt,b,b+.4))*.7,c:'#ff7a59'}],marks:[{k:'shield',x:cx(W(20)),y:yT+110,al:seg(lt,a+1.2,a+1.5)}]};
  X.ov=rcard(WORD('Ancre','Anchor','Ancla',44,'#7fe0a0'),pop(lt,b));},
 // 3. bloquer
 P09(lt,D,X){const a=D*.3;X.board={st:startState(),mv:[M(13,7,a,a+.8),M(13,7,a+.3,a+1.1)],hl:[{i:W(7),al:eo(seg(lt,a+1.1,a+1.4)),c:'#f6d77a'}],barHl:Math.sin(Math.PI*seg(lt,.2,a))*.8,marks:[{k:'tag',x:cx(W(7)),y:yB-140,t:'BAR POINT',al:seg(lt,a+1.3,a+1.6),bg:'#f6d77a',fs:20}]};note(X,lt,'13/7 13/7',[6,6],.1);},
 P10(lt,D,X){X.board={st:primeState(),hl:[4,5,6,7,8,9].map((n,k)=>({i:W(n),al:eo(seg(lt,D*.1+k*.15,D*.1+k*.15+.3)),c:'#7fe0a0'})),wall:{a:W(9),b:W(4),al:seg(lt,D*.5,D*.7)},marks:[{k:'tag',x:(cx(W(4))+cx(W(9)))/2,y:yB-215,t:'PRIME',al:seg(lt,D*.3,D*.45),bg:'#7fe0a0'},{k:'no',x:cx(W(2)),y:yB-120,al:seg(lt,D*.75,D*.85)}]};
  X.ov=rcard(`<div style="display:flex;gap:10px;justify-content:center;align-items:center"><span class="bf" style="font-size:72px;color:#f6d77a">6</span>${LOCK(70,'#f6d77a')}</div>`,pop(lt,D*.55));},
 P11(lt,D,X){const a=D*.35;X.board={st:startState(),hl:[{i:W(5),al:.5+.5*Math.sin(lt*5),c:'#fff6c8'},{i:W(8),al:eo(seg(lt,a,a+.3)),c:'#7fd3ff'},{i:W(6),al:eo(seg(lt,a,a+.3)),c:'#7fd3ff'}],paths:[arcI(W(8),W(5),90,'#7fd3ff',eo(seg(lt,a+.3,a+1))),arcI(W(6),W(5),70,'#7fd3ff',eo(seg(lt,a+.5,a+1.2)))],marks:[{k:'tag',x:cx(W(5)),y:yB-215,t:'?',al:seg(lt,.3,.6),bg:'#f6d77a'}]};
  X.ov=rcard(WORD('Constructeur','Builder','Constructor',40,'#7fd3ff'),pop(lt,a));},
 // 4. frapper, rentrer, tirs
 P12(lt,D,X){const a=D*.35;X.board={st:hitState(),mv:[{c:'b',f:W(5),t:'bar',a:a+.5,b:a+.9},M(13,5,a+.1,a+.9)],marks:[{k:'target',x:cx(W(5)),y:yB,al:lt<a+.6?eo(seg(lt,.3,.6)):0},{k:'burst',x:cx(W(5)),y:yB-110,t:'!',al:seg(lt,a+.9,a+1.2)}]};note(X,lt,'13/5*',[5,3],.1);},
 P13(lt,D,X){const a=D*.4;X.board={st:afterHit(),barHl:eo(seg(lt,.2,.6))*(lt<a+.8?1:0),mv:[{c:'b',f:'bar',t:W(3),a:a,b:a+.8}],zones:[{a:W(6),b:W(1),al:eo(seg(lt,a-.4,a))*.6,c:'#ff7a59'}],marks:[{k:'ok',x:cx(W(3)),y:yB-110,al:seg(lt,a+.9,a+1.2)}]};
  X.ov=rcard(`<div style="display:flex;gap:14px;justify-content:center;align-items:center">${mini('b',60)}<span class="bf" style="font-size:44px;color:#c9a86a">→</span>${dieSvg(3,'#fdfbf0',70)}</div>`,pop(lt,.2));},
 P14(lt,D,X){X.board=null;const a=D*.15,b=D*.55;
  X.ov=at(240,330,`<div class="card" style="width:340px;padding:22px;text-align:center;background:#7fe0a0">${NAME('Tir direct','Direct shot','Tiro directo',34)}<div style="display:flex;gap:10px;justify-content:center;align-items:center;margin-top:16px"><span class="bf" style="font-size:52px">≤ 6</span>${dieSvg(5,'#fdfbf0',70)}</div></div>`,pop(lt,a))+
  at(620,330,`<div class="card" style="width:340px;padding:22px;text-align:center;background:#7fd3ff">${NAME('Tir indirect','Indirect shot','Tiro indirecto',34)}<div style="display:flex;gap:10px;justify-content:center;align-items:center;margin-top:16px"><span class="bf" style="font-size:52px">7+</span>${dieSvg(4,'#fdfbf0',60)}<span class="bf" style="font-size:40px">+</span>${dieSvg(5,'#ff7a59',60)}</div></div>`,pop(lt,b));},
 // 5. la course
 P15(lt,D,X){const a=D*.2;X.board={st:raceState(),paths:[{d:RACE_W,p:eo(seg(lt,a,a+1.4)),c:'#7fe0a0',head:[TRX+26,yB-70,0]},{d:RACE_B,p:eo(seg(lt,a+.3,a+1.7)),c:'#ff7a59',head:[TRX+26,yT+70,0]}]};
  X.ov=rcard(WORD('Course','Race','Carrera',44,'#f6d77a'),pop(lt,D*.45));},
 P16(lt,D,X){const a=D*.55;const n=Math.round(167*eo(seg(lt,a,a+1.4)));X.board={st:startState(),labels:{n:24,al:.8}};
  X.ov=rcard(`<div class="bf" style="font-size:30px">Compte de pips</div><div style="font-weight:800;font-size:17px;color:#c9a86a">Pip count · Conteo de pips</div><div style="display:flex;gap:14px;justify-content:center;align-items:center;margin-top:14px">${mini('w',46)}<span class="bf" style="font-size:54px;color:#f6d77a">${n}</span>${mini('b',46)}<span class="bf" style="font-size:54px;color:#f6d77a">${n}</span></div>`,pop(lt,.2));},
 P17(lt,D,X){const a=D*.45;X.board={st:homeState(),zones:[{a:W(6),b:W(1),al:eo(seg(lt,.2,.6))*.6,c:'#7fe0a0'}],doorHl:Math.sin(Math.PI*seg(lt,a-.4,a+2.2)),mv:[M(6,'off',a,a+.6),M(5,'off',a+.5,a+1.1),M(4,'off',a+1,a+1.6)]};
  X.ov=rcard(`<div style="display:flex;gap:14px;justify-content:center;align-items:center">${STACK(15,90)}${OFFI(80)}${TROPHY(80)}</div>`,pop(lt,.2));},
 // 6. le videau
 P18(lt,D,X){X.board=null;const v=[2,4,8,16,32,64];const t0=D*.3,st=D*.08;X.ov=at(420,250,`<div style="transform:rotate(${Math.sin(lt*2)*6}deg)">${cubeSvg(64,190)}</div>`,pop(lt,.2))+
  `<div class="a" style="left:60px;top:430px;width:740px;display:flex;gap:14px;justify-content:center">${v.map((x,k)=>`<div style="${sc(pop(lt,t0+k*st))}">${cubeSvg(x,100)}</div>`).join('')}</div>`+rcard(WORD('Videau','Cube','Cubo',44,'#f6d77a'),pop(lt,D*.75));},
 P19(lt,D,X){const a=D*.35;X.board={st:startState(),cube:{x:F+HALF+BAR/2,y:BH/2,v:lt<a+.4?1:2,al:pop(lt,.2),r:(1-eo(seg(lt,a,a+.6)))*-180}};
  X.ov=rcard(`<div style="display:flex;gap:16px;justify-content:center;align-items:center"><span class="bf" style="font-size:64px;color:#f6d77a">×2</span>${cubeSvg(2,80)}</div>`,pop(lt,D*.55));},
 P20(lt,D,X){X.board=null;const a=D*.2,b=D*.6;
  X.ov=at(240,320,`<div class="card" style="width:340px;padding:22px;text-align:center;background:#7fe0a0">${NAME('Prendre','Take','Aceptar',38)}<div style="display:flex;gap:12px;justify-content:center;align-items:center;margin-top:16px">${ck(60)}${cubeSvg(2,70)}<span class="bf" style="font-size:46px">×2</span></div></div>`,pop(lt,a))+
  at(620,320,`<div class="card" style="width:340px;padding:22px;text-align:center;background:#ff7a59">${NAME('Passer','Pass','Rechazar',38)}<div style="display:flex;gap:12px;justify-content:center;align-items:center;margin-top:16px">${cr(60)}<span class="bf" style="font-size:46px">−1</span></div></div>`,pop(lt,b));},
 // 7. gagner
 P21(lt,D,X){X.board=null;X.ov=at(420,320,`<div class="card" style="padding:26px 46px;text-align:center">${TROPHY(130)}<div class="bf" style="font-size:64px;color:#0d3326;margin-top:8px">×1</div></div>`,pop(lt,.2))+rcard(WORD('Simple','Single game','Simple',40,'#fdfbf0'),pop(lt,D*.4));},
 P22(lt,D,X){X.board={st:gammonState(),doorHl:eo(seg(lt,.2,.6)),marks:[{k:'tag',x:TRX+26,y:yB-260,t:'15',al:seg(lt,.3,.6),bg:'#7fe0a0'}]};
  X.ov=rcard(`<div class="bf" style="font-size:46px">Gammon</div><div class="bf" style="font-size:72px;color:#f6d77a;${sc(pop(lt,D*.55))}">×2</div>`,pop(lt,.3));},
 P23(lt,D,X){X.board={st:bgState(),barHl:eo(seg(lt,.3,.7)),hl:[{i:W(3),al:eo(seg(lt,.3,.7)),c:'#ff7a59'}],marks:[{k:'target',x:cx(W(3)),y:yB,al:seg(lt,.3,.7)}]};
  X.ov=rcard(`<div class="bf" style="font-size:42px">Backgammon</div><div class="bf" style="font-size:72px;color:#ff7a59;${sc(pop(lt,D*.35))}">×3</div>`,pop(lt,.2));X.laugh=[D*.55,D*.75];},
 // 8. match, Crawford, ouverture, chouette
 P24(lt,D,X){X.board=null;X.ov=at(420,240,SCORE(3,2,5),pop(lt,.2))+at(420,450,SCORE(4,6,7),pop(lt,D*.55))+rcard(WORD('Match','Match','Match',44,'#7fd3ff'),pop(lt,D*.3));},
 P25(lt,D,X){X.board=null;const a=D*.4;X.ov=at(420,240,SCORE(4,2,5,0),pop(lt,.2))+at(420,450,`<div style="position:relative">${cubeSvg(2,150)}<div class="a" style="right:-30px;bottom:-20px;${sc(pop(lt,a+.4))}">${cr(90)}</div></div>`,pop(lt,a))+rcard(WORD('Crawford','Crawford','Crawford',42,'#f6d77a'),pop(lt,D*.65));},
 P26(lt,D,X){const a=D*.25;X.board={st:startState(),mv:[M(8,5,a,a+.8),M(6,5,a+.3,a+1.1)],hl:[{i:W(5),al:eo(seg(lt,a+1.1,a+1.4)),c:'#7fe0a0'}]};note(X,lt,'8/5 6/5',[3,1],.1);
  X.ov+=rcard(`<div style="display:flex;gap:14px;justify-content:center;align-items:center">${NAME('Ouverture','Opening','Apertura',34)}<span class="bf" style="font-size:64px;color:#f6d77a">15</span></div>`,pop(lt,D*.6),410,350);},
 P27(lt,D,X){X.board=null;const a=D*.3;X.ov=avAt('A',200,330,170,{pop:pop(lt,.2),role:'box',name:false})+at(330,330,`<span class="bf" style="font-size:54px;color:#c9a86a">VS</span>`,pop(lt,.5))+
  avAt('B',470,250,130,{pop:pop(lt,a),role:'cap',name:false})+avAt('C',600,370,120,{pop:pop(lt,a+.2),role:'team',name:false})+avAt('D',470,450,120,{pop:pop(lt,a+.4),role:'team',name:false})+
  rcard(WORD('Chouette','Chouette','Chouette',44,'#f6d77a'),pop(lt,D*.15));X.wave=[D*.7,D*.95];},
 // 9. conclusion
 P28(lt,D,X){X.board=null;const items=[[`<span class="bf" style="font-size:40px">Blot</span>${mini('w',44)}`,'#fdfbf0'],[`<span class="bf" style="font-size:40px">Prime</span>${LOCK(44,'#0d3326')}`,'#7fe0a0'],[`<span class="bf" style="font-size:40px">167</span>${mini('w',40)}`,'#7fd3ff'],[`${cubeSvg(2,56)}<span class="bf" style="font-size:40px">×2</span>`,'#f6d77a']];const t0=D*.12,st=Math.min(1.6,D*.7/4);
  X.ov=`<div class="a" style="left:60px;top:140px;width:740px;display:grid;grid-template-columns:1fr 1fr;gap:20px">${items.map((it,k)=>{const a=pop(lt,t0+k*st);return `<div class="card" style="position:relative;height:150px;display:flex;align-items:center;justify-content:center;gap:12px;background:${it[1]};${sc(a)}">${it[0]}<div class="a" style="right:-10px;top:-12px;${sc(pop(lt,t0+k*st+.35,.3))}">${ck(54)}</div></div>`;}).join('')}</div>`;X.clap=[D*.85,D];},
 P29(lt,D,X){X.board=null;X.ov=at(420,280,BOOK(220,'#7fd3ff'),pop(lt,.2))+at(420,500,`<div class="card bf" style="padding:12px 26px;font-size:30px">tickgammon.com/lexique-backgammon.php</div>`,pop(lt,D*.35));},
 P30(lt,D,X){X.board=null;X.ov=`<div class="a" style="left:70px;top:150px;width:720px">${lessonGrid(lt,.1)}</div>`+at(430,560,`<div class="card bf" style="padding:12px 30px;font-size:38px;background:#f6d77a">Saison 1 · Season 1 · Temporada 1</div>`,pop(lt,D*.6));X.conf=lt-D*.6;X.wave=[D*.6,D*.9];},
 P31(lt,D,X){X.board=null;X.ov=at(420,300,`<div class="card" style="padding:28px 46px;text-align:center;background:#ff7a59"><div style="display:flex;gap:10px;justify-content:center">${SPARK(60,'#fdfbf0')}${SPARK(46,'#f6d77a')}</div><div class="big" style="font-size:80px;color:#0d3326;margin-top:8px">Saison 2</div><div style="font-weight:800;font-size:24px;color:#0d3326;margin-top:8px">Season 2 · Temporada 2</div></div>`,pop(lt,.2))+at(420,520,`<span class="bf" style="font-size:40px;color:#f6d77a">…</span>`,pop(lt,D*.5));},
 P32(lt,D,X){X.board=null;const it=[LAPTOP(120),PHONE(120),WINPC(120)];X.ov=`<div class="a" style="left:60px;top:220px;width:740px;display:flex;gap:30px;justify-content:center">${it.map((x,k)=>`<div class="card" style="width:200px;height:200px;display:flex;align-items:center;justify-content:center;background:#0f4030;border:3px solid #c9a86a;${sc(pop(lt,.2+k*.3))}">${x}</div>`).join('')}</div>`+at(430,520,`<div class="card bf" style="padding:12px 30px;font-size:40px;background:#7fe0a0">tickgammon.com</div>`,pop(lt,D*.5));},
 P33(lt,D,X){X.board=null;X.top=0;const sa=Math.max(5.5,D*.42);const up=eo(seg(lt,0,1));
  X.owl={x:40,y:-20+(1-up)*420,s:.74,wave:lt<sa?[.6,2.6]:[sa,sa+2.2],wink:[D-2.4,D-2]};X.owlFront=1;
  X.ov=`<div class="a" style="left:560px;top:56px;width:680px">
  <div class="card bf" style="display:inline-block;padding:14px 32px;font-size:44px;background:#ff7a59;${sc(seg(lt,.3,.7))}">tickgammon.com</div>
  <div style="font-weight:800;font-size:26px;color:#d9e6dc;margin-top:14px;opacity:${eo(seg(lt,1,1.4))}">Web · Android · Windows</div>
  <div class="card" style="margin-top:24px;padding:16px 22px;display:flex;gap:18px;align-items:center;width:max-content;opacity:${eo(seg(lt,2.2,2.7))};transform:translateY(${(1-eo(seg(lt,2.2,2.7)))*30}px)">${TROPHY(70)}<div style="max-width:470px"><span class="pill" style="font-size:18px">Saison 1 ✓</span><div class="bf" style="font-size:30px;margin-top:6px">La saison 2 arrive bientôt</div><div style="font-weight:800;font-size:16px;color:#5b6f63">Season 2 is coming soon<br>La temporada 2 llega pronto</div></div></div></div>`+
  subscribe(lt,sa);X.conf=lt-(D-1.5);}
};

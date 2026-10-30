# Génère blocs_episode5_XX.txt (textes à coller dans ElevenLabs) depuis passages_xx.txt
splits=[(1,13),(14,25),(26,35)]
hdr={'fr':('FR','bloc{}.mp3','mêmes réglages que ton test.'),
     'en':('ENGLISH','bloc{}_en.mp3','mêmes réglages que pour le français.'),
     'es':('ESPAÑOL','bloc{}_es.mp3','mêmes réglages que pour le français.')}
for L,(tag,mp3,reg) in hdr.items():
    P={}
    for l in open(f'passages_{L}.txt',encoding='utf8'):
        if l.strip(): i,c,t=l.rstrip('\n').split('|',2); P[int(i[1:])]=t
    words=sum(len(t.replace('[laughs]','').split()) for t in P.values())
    out=[f"LEÇONS DE LA CHOUETTE — ÉPISODE 5 — TEXTES À COLLER DANS ELEVENLABS ({tag})",
         f"Voix : MIMI · Modèle : Eleven v4 · {reg}",
         "Copie UN bloc à la fois (tout ce qui est entre les lignes ===), sans les titres.",
         "Ne change rien au texte : les lignes vides servent de pauses entre les passages.",
         "Télécharge chaque résultat en MP3 et renomme-le : "+", ".join(mp3.format(k) for k in (1,2,3))+".",""]
    for k,(a,b) in enumerate(splits,1):
        body="\n\n".join(P[i] for i in range(a,b+1))
        out+=[f"########## BLOC {k} (P{a:02d} à P{b:02d}, {len(body)} caractères) → {mp3.format(k)} ##########","="*60,body,"="*60,""]
    open(f'blocs_episode5_{L.upper()}.txt','w',encoding='utf8').write("\n".join(out))
    print(L,words,'mots',[len("\n\n".join(P[i] for i in range(a,b+1))) for a,b in splits])

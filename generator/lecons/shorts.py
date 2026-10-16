import json,subprocess,sys
L=sys.argv[1]; SUF='' if L=='fr' else '_'+L
d=json.load(open(f'timeline{SUF}.json'));tl=d['tl']
src=f'lecon1_regles_{L}_16x9.mp4'
import os
for c in range(1,9):
    ps=[x for x in tl if x['ch']==c]
    a=max(0,ps[0]['t0']-0.15); b=ps[-1]['t0']+ps[-1]['d']+0.8; du=b-a
    out=f'shorts/lecon1_{L}_chap{c}_9x16.mp4'
    if os.path.exists(out): continue
    vf=f"[1:v]scale=1080:608,fade=t=in:st=0:d=0.3,fade=t=out:st={du-0.35:.2f}:d=0.35[v];[0:v][v]overlay=0:680,format=yuv420p[o]"
    subprocess.run(['ffmpeg','-loglevel','error','-y','-loop','1','-framerate','30','-i',f'shorts/bg_{L}_{c}.png','-ss',f'{a:.2f}','-t',f'{du:.2f}','-i',src,
      '-filter_complex',vf,'-map','[o]','-map','1:a','-af',f'afade=t=in:st=0:d=0.3,afade=t=out:st={du-0.5:.2f}:d=0.5','-t',f'{du:.2f}',
      '-c:v','libx264','-preset','medium','-crf','21','-c:a','aac','-b:a','160k','-movflags','+faststart',out],check=True)
    print(out,round(du,1))

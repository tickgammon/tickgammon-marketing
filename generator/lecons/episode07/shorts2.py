import json,subprocess,sys,os
L=sys.argv[1]
tl=json.load(open(f'timeline_{L}.json'))['tl']
src='lecon7_ordinateur_16x9.mp4'
os.makedirs('shorts2out',exist_ok=True)
for c in range(1,9):
    ps=[x for x in tl if x['ch']==c]
    a=max(0,ps[0]['t0']-0.15); b=ps[-1]['t0']+ps[-1]['d']+0.8; du=b-a
    out=f'shorts2out/lecon7_{L}_chap{c}_9x16.mp4'
    if os.path.exists(out): continue
    vf=f"[1:v]scale=1080:608,fade=t=in:st=0:d=0.3,fade=t=out:st={du-0.35:.2f}:d=0.35[v];[0:v][v]overlay=0:680,format=yuv420p[o]"
    subprocess.run(['ffmpeg','-loglevel','error','-y','-loop','1','-framerate','30','-i',f'shorts2/bg_{L}_{c}.png','-ss',f'{a:.2f}','-t',f'{du:.2f}','-i',src,'-ss',f'{a:.2f}','-t',f'{du:.2f}','-i',f'mix_{L}.wav',
      '-filter_complex',vf,'-map','[o]','-map','2:a','-af',f'afade=t=in:st=0:d=0.3,afade=t=out:st={du-0.5:.2f}:d=0.5','-t',f'{du:.2f}',
      '-c:v','libx264','-preset','medium','-b:v','8M','-maxrate','10M','-bufsize','16M','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',out],check=True)
    print(out,round(du,1))

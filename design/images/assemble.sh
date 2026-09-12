#!/usr/bin/env bash
# Assemble: clip1 + clip2 + clip3 (8 s each) with 0.8 s crossfades, end card 4 s with 1 s fade-in and 1 s fade to black, music + soft ambient.
set -e
FF=$(python3 -c "import imageio_ffmpeg as f; print(f.get_ffmpeg_exe())")
X=0.8; C=8; E=4
T1=$(python3 -c "print($C-$X)")            # start of xfade 1
T2=$(python3 -c "print(2*$C-2*$X)")        # start of xfade 2
T3=$(python3 -c "print(3*$C-3*$X)")        # start of xfade to end card (video length before card: 3C-2X; card fades in over 1 s)
TOTAL=$(python3 -c "print(3*$C-3*$X+$E)")  # total duration
$FF -v error -y \
  -i clip1.mp4 -i clip2.mp4 -i clip3.mp4 -loop 1 -t $E -i endcard.png -i music.mp3 \
  -filter_complex "
   [0:v]settb=AVTB,fps=24,format=yuv420p[v0];[1:v]settb=AVTB,fps=24,format=yuv420p[v1];[2:v]settb=AVTB,fps=24,format=yuv420p[v2];
   [3:v]scale=1920:1080,settb=AVTB,fps=24,format=yuv420p,fade=t=out:st=$(python3 -c "print($E-1)"):d=1[v3];
   [v0][v1]xfade=transition=fade:duration=$X:offset=$T1[x1];
   [x1][v2]xfade=transition=fade:duration=$X:offset=$T2[x2];
   [x2][v3]xfade=transition=fade:duration=1:offset=$(python3 -c "print(3*$C-2*$X-1)")[vout];
   [0:a][1:a]acrossfade=d=$X[a1];[a1][2:a]acrossfade=d=$X[amb0];[amb0]apad=whole_dur=$TOTAL,volume=0.30[amb];
   [4:a]atrim=0:$TOTAL,afade=t=in:st=0:d=1.5,afade=t=out:st=$(python3 -c "print($TOTAL-3.5)"):d=3.5,volume=0.9[mus];
   [amb][mus]amix=inputs=2:duration=first:normalize=0[aout]" \
  -map "[vout]" -map "[aout]" -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart -t $TOTAL huis-hinterglemm-1080.mp4
$FF -v error -y -i huis-hinterglemm-1080.mp4 -vf scale=1280:720 -c:v libx264 -preset slow -crf 27 -pix_fmt yuv420p -c:a aac -b:a 96k -movflags +faststart huis-hinterglemm-720.mp4
$FF -v error -y -i huis-hinterglemm-1080.mp4 -ss 1 -frames:v 1 -q:v 3 huis-hinterglemm-poster.jpg
$FF -v error -y -i huis-hinterglemm-1080.mp4 -vf "select='not(mod(n\,72))',scale=384:-1,tile=9x1" -frames:v 1 huis-hinterglemm-strip.jpg
ls -la huis-hinterglemm-1080.mp4 huis-hinterglemm-720.mp4 | awk '{print $9, $5/1048576 " MB"}'; $FF -i huis-hinterglemm-1080.mp4 2>&1 | grep Duration

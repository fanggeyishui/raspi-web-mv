nowtime=`date +%s`
path=/home/pi/Pictures/mvdir/
raspivid -t 5000 -o - > v.h264
MP4Box -add v.h264  $path$nowtime.mp4

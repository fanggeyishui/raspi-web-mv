# raspi-web-mv
树莓派用来采集视频的命令：
  raspistill -t 2000 -o image.jpg
  raspivid -l -o tcp://192.168.1.1:3333树莓派tcp输出
  raspivid -o - -t 0 -w 640 -h 360 -fps 25|cvlc -vvv stream:///dev/stdin --sout,mux=ts,dst=:8090}' :demux=h264      树莓派录像加vlc  （https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
  
  
  
树莓派转MP4
  sudo apt-get install gpac
  MP4Box -add filename.h264 filename.mp4
  
前端：不断播放新的视频js  
  video id="myvideo" src="xx.mp4"》《/video》
  myvideo.onended = function(){
  this.src= "yy.mp4";

  }

调用shell命令
  import os
  os.system('./print.sh&')
  while 1:
          print('cmd')
          sleep(2)





200616问题方法总结

获取当前网址window.location.href
由于浏览器相同url会存在缓存，因此每次视频应传递一个不同的url
vedio标签id可以拿来直接指代vedio对象？
摄像头要牢固不然会断开

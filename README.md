# piPictureSender


라즈베리파이 카메라 촬영과 이메일로 동영상 및 사진 전송과 웹 서버 구성  
[https://jeongchul.tistory.com/433](https://jeongchul.tistory.com/433)  


이더넷을 이용하여 라즈베리 파이에서 PC로 사진 전송하는 법  
[https://jayharvey.tistory.com/6](https://jayharvey.tistory.com/6)  

라즈베리파이로 유튜브  
[http://blog.naver.com/PostView.nhn?blogId=roboholic84&logNo=221326060315](http://blog.naver.com/PostView.nhn?blogId=roboholic84&logNo=221326060315)

raspivid -o - -t 0 -vf -hf -fps 10 -b 500000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/k509-aj7e-emev-f1m5-ajwt

이 레포지코리 안에 있는 picam.py파일을 파이썬으로 실행시키면 라즈베리파이에서 파이썬을 이용해 usb웹캠을 구동시킬 수 있음  


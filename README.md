# AI_smart_VolumeControl

### The advantage of artificial intelligence (AI) and machine learning (ML) to control volume of ur TV, computers and many smart devices using a cameras making them smarter . AI, Because it learns through experience, the more it is used, the smarter it becomes. 
### You can still build a home theatre setup using large speakers and soundbars, or your computers, raspberry pis, jetson nanos , your smart TVs, your CARs etc..



**dependencies:**

  python3\
  opencv\
  google's mediapipe Hands



**mediapipe hands ?**

MediaPipe Hands is a high-fidelity hand and finger tracking solution. It employs machine learning (ML) to infer 21 3D landmarks of a hand from just a single frame. Whereas current state-of-the-art approaches rely primarily on powerful desktop environments for inference, our method achieves real-time performance on a mobile phone, and even scales to multiple hands


# here both windows and linux users can try out.

**USAGE:**
```
windows:
pip install opencv-python -u
pip install mediapipe
pip install pycaw

python vol_cont-WINDOWS.py
```
pycaw ?

[Python Core Audio Windows Library, working for both Python2 and Python3](https://github.com/AndreMiras/pycaw)

```
linux: rasp/ubuntu/jetson nano etc..
pip3 install opencv-python -u
pip3 install mediapipe
sudo apt-get install libasound2-dev
pip3 install pyalsaaudio

python3 vol_cont-LINUX.py
```

alsaaudio ?

[Python Core Audio Library,for linux machines working for both Python2 and Python3](https://github.com/larsimmisch/pyalsaaudio)





**demo:**

![Alt Text](output.gif)


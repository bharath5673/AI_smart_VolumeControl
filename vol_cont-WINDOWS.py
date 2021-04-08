import cv2
import time
import numpy as np
import HandTrack as htm
import math 

#picaw //python core audio libraries for windows.
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


wCam, hCam = 640,480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0


detector = htm.handDet(detectionCon=0.7,maxHands=1)

#volume utils
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(-20.0, None)


minVol=0
maxVol=0


#vol params
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

tipIds = [4,8,12,16,20]


while True:
	success, img = cap.read()
	img = detector.findHands(img)
	lmList = detector.findPosition(img, draw=False)
	# print(lmList)

	if len(lmList) !=0:

		finger = []

		if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
			finger.append(1)
		else:
			finger.append(0)


		for id in range(1,5): 

			if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
				finger.append(1)
			else:
				finger.append(0)

		# print(finger)

		totalFingers = finger.count(1)
		# print(totalFingers)

		if totalFingers == 2 :
			# time.sleep(2)
			# cv2.waitKey(100)
			# print('Volume sign detected')
			cv2.putText(img, 'Volume sign detected',(200,450), cv2.FONT_HERSHEY_DUPLEX,
				1,(255,255,0),3)


			# print(lmList[4], lmList[8])
			x1, y1 = lmList[4][1], lmList[4][2]
			x2, y2 = lmList[8][1], lmList[8][2] 
			# print(x1,y1,x2,y2)

			cx,cy = (x1 +x2) //2, (y1+y2) //2### putting circle in between

			cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
			cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
			# cv2.line(img, (x1, y1), (x2,y2), (255, 0 ,255), 3)
			# cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)

			length = math.hypot(x2 -x2,y2-y1)
			# print(length)
			if length<50:
				cv2.circle(img, (cx,cy),15, (0,255,0), cv2.FILLED)

			#hand range 50 -300
			#volume Range 65-0
			vol = np.interp(length, [50,300], [minVol,maxVol])
			volBar = np.interp(length, [50,300], [400, 150])
			volBar = np.interp(length, [50,300], [400, 150])
			volPer = np.interp(length, [50,300], [0, 100])


			volume.SetMasterVolumeLevel(vol, None)



			#### overlay space     
			oalpha = 0.7
			overlay = img.copy()
			output = img.copy()
			cv2.rectangle(overlay,(43, 143), (92, 410), (0,0,0), -1)	
			cv2.addWeighted(overlay, oalpha, output, 1- oalpha, 0, img)





			cv2.rectangle(img, (50, 150), (85, 400), (0,255,0), 3)
			cv2.rectangle(img, (50, int(volBar)),(85, 400), (0,255,0), cv2.FILLED)
			cv2.putText(img, f'{int(volPer)} %',(40,450), cv2.FONT_HERSHEY_DUPLEX,
				0.7,(0,0,255),2)

		# cv2.waitKey(100) 	


	cTime = time.time()
	fps = 1 / (cTime-pTime)
	pTime = cTime

	cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_DUPLEX,
			1,(255,0,0),3)
	cv2.imshow("Img",img)
	# cv2.waitKey(1)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

cap.release()
cv2.destroyAllWindows()
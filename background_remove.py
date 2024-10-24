import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import numpy as np
import time
import os

video = cv2.VideoCapture(0)
segmentor = SelfiSegmentation()

folder = ('K:\Python\Computer Vision Detection Projects\Background Removal\Data')
imglist = os.listdir('K:\Python\Computer Vision Detection Projects\Background Removal\Data')
img = []
for path in imglist:
    imgPath = cv2.imread(f'{folder}\{path}')
    imgPath = cv2.resize(imgPath, (640, 480))
    img.append(imgPath)
imgIndex=0
print(img)
pTime=0
while True:
    r, frame = video.read()

    if r==True:
        frame  = cv2.resize(frame, (640, 480))
        frame = cv2.flip(frame, 1)

        # selfsegmentation
        removedBG = segmentor.removeBG(frame, img[imgIndex], cutThreshold=0.2)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(frame, str(f'FPS: {int(fps)}'), (5, 20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,255), 2)
        cv2.putText(removedBG, str(f'FPS: {int(fps)}'), (5, 20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,255), 2)

        h = np.hstack((frame, removedBG))
        cv2.imshow('Background Removed', h)

        key = cv2.waitKey(1) & 0xff

        if key == ord('d'):
            imgIndex = (imgIndex+1) % len(img)
        
        elif key == ord('a'):
            imgIndex = (imgIndex-1) % len(img)

        elif key == ord('p'):
            break

    else:
        break

video.release()
cv2.destroyAllWindows()
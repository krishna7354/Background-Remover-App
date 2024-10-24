import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import numpy as np
import time
import os


class BackgroundRemover:
    def __init__(self, video_source=0, folder_path='K:\Python\Computer Vision Detection Projects\Background Removal\Data'):

        self.video = cv2.VideoCapture(video_source)
        self.segmentor = SelfiSegmentation()
        self.folder_path = folder_path
        self.img_list = os.listdir(folder_path)
        self.backgrounds = self.load_background_images()
        self.img_index = 0
        self.pTime = 0

    def load_background_images(self):

        img = []
        for path in self.img_list:
            img_path = cv2.imread(f'{self.folder_path}\\{path}')
            img_path = cv2.resize(img_path, (640, 480))
            img.append(img_path)
        return img

    def run(self):

        while True:
            r, frame = self.video.read()

            if r:
                frame = cv2.resize(frame, (640, 480))
                frame = cv2.flip(frame, 1)

                removedBG = self.segmentor.removeBG(frame, self.backgrounds[self.img_index], cutThreshold=0.2)

                cTime = time.time()
                fps = 1 / (cTime - self.pTime)
                self.pTime = cTime

                cv2.putText(frame, f'FPS: {int(fps)}', (5, 20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
                cv2.putText(removedBG, f'FPS: {int(fps)}', (5, 20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)

                h = np.hstack((frame, removedBG))
                cv2.imshow('Background Removed', h)

                key = cv2.waitKey(1) & 0xff

                if key == ord('d'):  
                    self.img_index = (self.img_index + 1) % len(self.backgrounds)
                elif key == ord('a'):
                    self.img_index = (self.img_index - 1) % len(self.backgrounds)
                elif key == ord('p'): 
                    break
            else:
                break

        self.video.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    remover = BackgroundRemover()
    remover.run()

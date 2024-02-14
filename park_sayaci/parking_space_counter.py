import cv2
import pickle
import numpy as np 

class parking_counter():
    def __init__(self):
        self.width = 80
        self.height = 35

        self.cap = cv2.VideoCapture("OpenCV-Udemy\\Goruntu_isleme_projeleri\\park_sayaci\\park_video.mp4")

        with open(file="CarParkPosition", mode="rb") as f:
            self.posList = pickle.load(file=f)

        while True:
            self.success, self.img = self.cap.read()
            self.img = cv2.rotate(self.img, cv2.ROTATE_90_CLOCKWISE)
            self.img = cv2.resize(src=self.img, dsize=(480,720))

            
            self.imgGray = cv2.cvtColor(src=self.img, code=cv2.COLOR_BGR2GRAY)
            self.imgBlur = cv2.GaussianBlur(src=self.imgGray, ksize=(3,3), sigmaX=1)
            self.imgThreshold = cv2.adaptiveThreshold(src=self.imgBlur, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType=cv2.THRESH_BINARY_INV, blockSize=25, C=16)
            self.imgMedian = cv2.medianBlur(src=self.imgThreshold, ksize=7)
            self.imgDilate = cv2.dilate(src=self.imgMedian, kernel=np.ones((3,3)), iterations=2)

            
            self.checkParkSpace(self.imgDilate)

           
            self.out_rec = False
            cv2.imshow(winname="record", mat=self.img)
            if cv2.waitKey(150) & 0xFF == ord("q"):
                break



    def checkParkSpace(self,frame):
        self.frame = frame
        self.spaceCounter = 0

        for pos in self.posList:
            x, y = pos

            self.img_crop = self.frame[y:y+self.height, x:x+self.width]
            self.count = cv2.countNonZero(src=self.img_crop)
            #print("self.count:",self.count)

            if self.count < 380:
                color = (0,255,0)
                self.spaceCounter += 1
                

            elif self.count > 380:
                color = (0,0,255)

            cv2.rectangle(img=self.img, pt1=pos, pt2=(pos[0] + self.width, pos[1] + self.height), color=color, thickness=2)

        cv2.putText(img=self.img, text=f"free:{self.spaceCounter}/{len(self.posList)}", org=(160,50),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(255,0,0),thickness=2)

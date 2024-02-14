import cv2
import pickle


class parking_picker():
    def __init__(self):
        self.width = 80
        self.height = 35

        try:
            with open(file="CarParkPosition", mode="rb") as f:
                self.posList = pickle.load(file=f)
        except:
            self.posList = []


    def mouseClick(self, events, x, y, flags, params):
        self.events = events
        self.x = x 
        self.y = y
        self.flags = flags
        self.params = params

        if self.events == cv2.EVENT_LBUTTONDOWN:
            self.posList.append((self.x,self.y))

        if self.events == cv2.EVENT_RBUTTONDOWN:
            for i,pos in enumerate(self.posList):
                x1, y1 = pos
                if x1 < self.x < x1 + self.width and y1 < self.y < y1 + self.height:
                    self.posList.pop(i)

        with open (file="CarParkPosition", mode="wb") as f:
            pickle.dump(obj=self.posList, file=f)

    def start(self):
        while True:
            self.img = cv2.imread(filename="OpenCV-Udemy\\Goruntu_isleme_projeleri\\park_sayaci\\resim.png")
            self.img = cv2.resize(src=self.img, dsize=(480,720))

            # print("poslist:", self.posList)

            for pos in self.posList:
                cv2.rectangle(img=self.img, pt1=pos, pt2=(pos[0] + self.width, pos[1] + self.height), color=(0,255,0), thickness=2)

            cv2.imshow(winname="resim", mat=self.img)
            cv2.setMouseCallback("resim", self.mouseClick)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    

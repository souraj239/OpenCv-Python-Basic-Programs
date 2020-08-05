import cv2
import numpy as np

def stackImages(scale,imgArray):

    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>500:                                                                #To Minimize noise
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)                                                 #Approx number of corner points                
            print(len(approx))
            objCorner=len(approx)
            x,y,w,h=cv2.boundingRect(approx)

            if objCorner==3:
                ObjectType="TRI"
            elif objCorner==4:
                aspectRatio=w/float(h)
                if aspectRatio>0.95 and aspectRatio<1.05:
                    ObjectType="Squar"
                else:
                    ObjectType="Rect"
            elif objCorner>5:
                ObjectType="Circle"
            else:
                ObjectType="None"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,ObjectType,((x+(w//2)-10),(y+(h//2)-5)),cv2.FONT_HERSHEY_COMPLEX,0.8,(1,1,5),2)
    
img=cv2.imread("Resources/shapes.png")
imgContour=img.copy()
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)
imgBlank=np.zeros_like(img)

getContours(imgCanny)

#cv2.imshow("imgGray",imgGray)
#cv2.imshow("BlurredImage",imgBlur)
imgStack=stackImages(0.6,([img,imgGray,imgBlur],[imgCanny,imgBlank,imgContour]))
cv2.imshow("Stacked",imgStack)
cv2.waitKey(0)
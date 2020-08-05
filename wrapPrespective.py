import cv2
import numpy as np

img=cv2.imread("Resources/cards.jpg")

width,height=350,250                                                        #Aspect ratio of a playing card
pts1=np.float32([[330,95],[471,197],[159,259],[302,362]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOut=cv2.warpPerspective(img, matrix,(height,width))

cv2.imshow("Output",img)
cv2.imshow("OutputWarp",imgOut)
cv2.waitKey(0)
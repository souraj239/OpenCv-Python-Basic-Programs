import cv2
import numpy as np

img= np.zeros((512,512,3),np.uint8)                                            #creating a black image

#img [:]=255,0,0                                                               #changing all the pixels to blue

#cv2.line(img,(0,0),(300,300),(0,255,0),3)                                     #drawing a line from (0,0) to (300,300) in green color and thickness=3
cv2.line(img,(0,0),(img.shape[1], img.shape[0]),(0,255,0),3)                   #diagonal line across the image 
cv2.rectangle(img,(128,128),(384,384),(0,0,255),cv2.FILLED)                    #Rectange drawing from (128,128) to (384,384) and filled it with red color
cv2.circle(img,(256,256),70,(255,255,0),cv2.FILLED)                            #Circle as (256,256) as centre and radius=50 and filled                                                   
cv2.putText(img," OpenCV ",(180,260),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,255),2)  #add text to the image at position (180,260)

cv2.imshow("Output",img)
cv2.waitKey(0) 
import cv2
import numpy as np

kernel=np.ones((5,5),int)

img=cv2.imread("Resources/image.jpg")
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)               #Image to Black and white 
imgBlur= cv2.GaussianBlur(img,(9,9),0)                      #Blurred Image
imgCanny=cv2.Canny(img,150,150)                             #Edge Detection
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)       #increase canny thickness
imgEroded=cv2.erode(imgDialation,kernel,iterations=2)       #Reduce the thickness of the canny

#cv2.imshow("OutputGrayscale",imgGray)
#cv2.imshow("BlurredImg",imgBlur)
#cv2.imshow("CannyImg",imgCanny)
#cv2.imshow("DialationImg",imgDialation)
cv2.imshow("ErosionImg",imgEroded)
cv2.waitKey(0)
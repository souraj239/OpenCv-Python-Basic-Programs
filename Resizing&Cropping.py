import cv2

img=cv2.imread("Resources/car.jpg")
print(img.shape)
imgResize=cv2.resize(img,(300,200))                #Image Resize
print(imgResize.shape)

imgCropped= imgResize[50:150,50:250]               #Cropping the Resized image using simple array slicing tool. [a:b,x:y], where a=> starting range of length and b=> ending range of length. same with x,y for length

cv2.imshow("Output",img)
cv2.imshow("ResizeOutput",imgResize)
cv2.imshow("imgCropped",imgCropped)
cv2.waitKey(0)
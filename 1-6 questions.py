import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
img = cv2.imread("C:\\Users\\Girishma reddy\\OneDrive\\Desktop\\open cv\\image1.jpg")
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(img,(7,7),0)
canny=cv2.Canny(img,100,200)
dilation=cv2.dilate(img,kernel,iterations=10)
eroded=cv2.erode(img,kernel,iterations=2)
cv2.imshow("Grayscale",grey)
cv2.imshow("imgBlur",blur)
cv2.imshow("canny",canny)
cv2.imshow("dilate",dilation)
cv2.imshow("eroded",eroded)
cv.waitKey(0)




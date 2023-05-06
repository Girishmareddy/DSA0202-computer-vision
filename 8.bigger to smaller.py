import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)

img = cv2.imread("C:\\Users\\Girishma reddy\\OneDrive\\Desktop\\open cv\\image1.jpg", cv2.IMREAD_COLOR)
img1 = cv2.resize(img,(700,700))
img2 = cv2.resize(img,(1500,1500))
img3 = cv2.resize(img,(500,500))
cv2.imshow("image", img1)
cv2.imshow("image", img2)
cv2.imshow("image", img3)
cv2.waitKey(0)

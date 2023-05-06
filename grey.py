import cv2
img = cv2.imread("C:\\Users\\Girishma reddy\\OneDrive\\Desktop\\open cv\\image1.jpg")
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey_image",grey)







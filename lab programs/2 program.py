import cv2
img=cv2.imread("C:\\Users\\reddy\\Downloads\\flower.jpg")
cv2.imshow("Image window",img)



#coloer image to gray#
import cv2
gray=cv2.crtcolor(img,cv2.color_BGR2GRAY)
cv2.inshow("image",gray)

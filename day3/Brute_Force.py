import cv2
img1=cv2.imread('pic2.jpeg')
img2=cv2.imread('bpic2.jpeg')
orb=cv2.ORB_create()
kp1,des1=orb

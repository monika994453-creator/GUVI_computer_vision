import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("pic.jpg")
rows,cols=image.shape[:2]
(h, w) = image.shape[:2]

M = np.float32([[1,0,-10],[0,1,0]])
translate = cv2.warpAffine(image,M,(cols,rows))

RM = cv2.getRotationMatrix2D((w//2,h//2),45,1.0)
rotated = cv2.warpAffine(image, RM, (w,h))

scaled = cv2.resize(image,None,fx=2,fy=2)

plt.imshow(cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB))

plt.show()

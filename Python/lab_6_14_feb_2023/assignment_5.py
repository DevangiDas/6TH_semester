import numpy as np
import cv2 as cv
kernel=np.ones((3,3),np.float32)/9
img=cv.imread('C:/Users/DDas/Downloads/pattern_two.jfif',0)
dst=cv.filter2D(img,-1,kernel)
cv.imshow("resized",dst)
cv.waitKey(0)
cv.destroyAllWindows()
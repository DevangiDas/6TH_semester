# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:23:09 2023

@author: DDas
"""
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('D:/Programing_works/6th_semester_work/Python/lab_6_14_feb_2023/abs_idea.jpg',0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray') 
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#cv.imshow("Original Image", img) 
#plt.title('Original Image')
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

# import cv2  
# img = cv2.imread('D:/Programing_works/6th_semester_work/Python/lab_6_14_feb_2023/abs_idea.jpg')  
# edges = cv2.Canny(img, 100, 200)  
  
# cv2.imshow("Edge Detected Image", edges)  
# cv2.imshow("Original Image", img)  
# cv2.waitKey(0)  # waits until a key is pressed  
# cv2.destroyAllWindows()  # destroys the window showing image 
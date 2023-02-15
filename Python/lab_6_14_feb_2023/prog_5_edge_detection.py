# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:23:09 2023

@author: DDas
"""

import cv2  
img = cv2.imread(r'D:/VSCode/6th_sem_python/lab_6_14_feb_2023/abs_idea.jpg')  
edges = cv2.Canny(img, 100, 200)  
  
cv2.imshow("Edge Detected Image", edges)  
cv2.imshow("Original Image", img)  
cv2.waitKey(0)  # waits until a key is pressed  
cv2.destroyAllWindows()  # destroys the window showing image 
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 10:10:33 2023

@author: DDas
"""
#import pandas as pd
#import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
#img = cv.imread("D:/Programing_works/6th_semester_work/Python/lab_7_21_feb/coin.jpeg", 1)
img = cv.imread("D:/Programing_works/6th_semester_work/Python/lab_7_21_feb/japan.jpg",1)
#img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray = cv.cvtColor(img.copy(),cv.COLOR_BGR2GRAY)
#plt.imshow(gray)
ret, thresh = cv.threshold(gray, 125, 255, 0)
#plt.imshow(thresh)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(contours)
#contours = sorted(contours,key = cv.contourArea,reverse = True)
copy_img = img.copy()
final = cv.drawContours(copy_img,contours,-1,(255,0,255),2)
plt.imshow(copy_img)
cv.waitKey(1)
cv.destroyAllWindows()




# gray = cv.cvtColor(img.copy(),cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(gray, 125, 255, 0)
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# copy_img = img.copy()
# cv.drawContours(copy_img,contours,-1,(255,0,0),2)
# titles = ['original','contours']
# imgs = [img, copy_img]
# for i in range (2):
#     plt.subplot(1,2,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.title(titles[i])
#     plt.imshow(imgs[i])
# plt.show()
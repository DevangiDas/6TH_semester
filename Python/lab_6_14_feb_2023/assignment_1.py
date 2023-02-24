# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 22:33:48 2023

@author: DDas
"""

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np 

img = cv.imread('C:/Users/DDas/Downloads/pattern_two.jfif',0)

print(type(img))
print(img.shape)
px = img[100,100]
print(px)

cv.imshow('Image',img)
cv.waitKey()
cv.destroyAllWindows()
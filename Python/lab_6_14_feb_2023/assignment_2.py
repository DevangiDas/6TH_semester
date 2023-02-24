# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 22:34:34 2023

@author: DDas
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/DDas/Downloads/pattern_two.jfif',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
print(type(img))
flat= img.flatten()
print("flatten",flat)
print(np.cov(flat))

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
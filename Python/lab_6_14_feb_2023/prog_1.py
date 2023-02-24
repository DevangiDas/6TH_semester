import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('D:/Programing_works/6th_semester_work/Python/lab_6_14_feb_2023/abs_idea.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')

plt.show()
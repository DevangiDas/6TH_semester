#import pandas as pd
#import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
img = cv.imread("D:/Programing_works/6th_semester_work/Python/lab_7_21_feb/coin.jpeg", 1)
#img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
plt.imshow(img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (7, 7), 0)
(T, thresh) = cv.threshold(blurred, 200, 255, cv.THRESH_BINARY)
cv.imshow("Threshold Binary", thresh)
cv.waitKey(0)
cv.destroyAllWindows()


#the code inverts the above threshold pic i.e from black it becomes white
(T, threshInv) = cv.threshold(blurred, 200, 255,cv.THRESH_BINARY_INV)
cv.imshow("Threshold", threshInv)
cv.waitKey(0)
cv.destroyAllWindows()
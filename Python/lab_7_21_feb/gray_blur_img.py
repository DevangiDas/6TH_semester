import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
img = cv.imread("D:/Programing_works/6th_semester_work/Python/lab_7_21_feb/coin.jpeg", 1)
#img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
plt.imshow(img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (7, 7), 0)
cv.imshow("Gaussian blurred", blurred)
cv.waitKey(0)
cv.destroyAllWindows()
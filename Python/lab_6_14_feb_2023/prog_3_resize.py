import cv2 
#import numpy as np
#from matplotlib import pyplot as plt 
  
img = cv2.imread(r'D:/VSCode/6th_sem_python/lab_6_14_feb_2023/abs_idea.jpg', 1)  
scale = 60  
width = int(img.shape[1] * scale / 100)  
height = int(img.shape[0] * scale / 100)  
dim = (width, height)  
# resize image  
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)  
  
print('Resized Dimensions : ', resized.shape)  
  
cv2.imshow("Resized image", resized)  
cv2.waitKey(0)  
cv2.destroyAllWindows()
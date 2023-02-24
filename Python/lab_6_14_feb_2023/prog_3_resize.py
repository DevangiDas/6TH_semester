import cv2 
#import numpy as np
#from matplotlib import pyplot as plt 
  
img = cv2.imread(r'D:/Programing_works/6th_semester_work/Python/lab_6_14_feb_2023/abs_idea.jpg', 1)  
scale = 56
width = int(img.shape[1] * scale / 100)  
height = int(img.shape[0] * scale / 100)  
dim = (width, height)  
# resize image  
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)  
  
print('Resized Dimensions : ', resized.shape) 
print('org Dimensions : ', img.shape) 
diff =tuple(map(lambda i, j: i - j, img.shape, resized.shape))
print("difference in size",diff)
  
cv2.imshow("Resized image", resized)  
cv2.waitKey(0)  
cv2.destroyAllWindows()
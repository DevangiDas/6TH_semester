#warp to create array of 2 3*3 matrice sfrom to given vectors

vec_1<-c(48,21,60,12,28)
vec_2<-c(27, 47, 66, 99, 59, 35, 72, 77, 91, 76, 11, 93)
vec_3<-c(26, 41, 94, 5, 25, 49, 10, 16, 31, 69)

arr<-array(c(vec_1,vec_2,vec_3),dim = c(3,3,2))
print(arr)
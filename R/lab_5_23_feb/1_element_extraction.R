# warp to create an array of 2 3*3 matrices print the 2 row of the 2 matrix of the array and element in the 3rd row and 3 col of 1st matrix

arr<-array(c(1:9,11:19),dim=c(3,3,2))
print(arr)
extract_1<- arr[2,,2]
print(extract_1)
extract_2<-arr[3,3,1]
print(extract_2)
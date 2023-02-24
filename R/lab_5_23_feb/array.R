#(2,2,3) here  3 matrices each conating 2 rows and 2 columns

a<- array(c(1:9))
arr<-array(c(11:14,21,24,31:34),dim=c(2,2,3))
print(arr)
rname = c('r1','r2','r3')
colname = c('c1','c2','c3')
matname = c('m1','m2','m3')
arr<-array(c(1:9),dim=c(2,2,3),dimnames = list(rname,colname,matname))
#2 row all col
x<-arr[2,,1]
print(x)
#3 row 3 col from both matrix
#var_name = apply(array_name,c(1 or 2),function)


#questions on array
# warp to create an array of 2 3*3 matrices print the 2 row of the 2 matrix of the array and element in the 3rd row and 3 col of 1st matrix
#warp to create an array using 4 given cols 3 given rows nd 2 given tables and display the content of the array
#warp  to create an array of having 3 dimension now calculate the sum of the rows across all the matrices
#warp to create max and min elements from the rows and colums
#warp to create array of 2 3*3 matrice sfrom to given vectors
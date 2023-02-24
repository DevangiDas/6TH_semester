#warp  to create an array of having 3 dimension now calculate the sum of the rows across all the matrices

arr<-array(c(1:9,11:19,21:29),dim=c(3,3,3))
print(arr)
#rowSums(arr)
sums<-apply(arr,c(1),sum)
print(sums)

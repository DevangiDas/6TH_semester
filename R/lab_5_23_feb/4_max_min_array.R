#warp to create max and min elements from the rows and colums

arr<-array(c(1:9,11:19),dim=c(3,3,2))
print(arr)
col_max<-apply(arr,c(2),max)
row_max<-apply(arr,c(1),max)
col_min<-apply(arr,c(2),min)
row_min<-apply(arr,c(1),min)
print("max in col:")
print(col_max)
print("max in row:")
print(row_max)
print("min in col:")
print(col_min)
print("min in row")
print(row_min)
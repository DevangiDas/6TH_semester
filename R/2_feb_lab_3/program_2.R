vector1 <- c(1,2,3)
vector2 <- c(4,5,6)
vector3 <- c(7,8,9)
mymatrix <- matrix(c(vector1,vector2,vector3),nrow =3)
print(mymatrix)

new_mat<-matrix(c(0,0,0),nrow=1,ncol=3)
for(i in 1:3){
  new_mat[1,i]<-mymatrix[i,i]
}

print(new_mat)
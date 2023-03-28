mat <- matrix(c(1,2,3,2,4,5,3,5,6),nrow = 3,ncol = 3)
print(mat)

trans <- matrix(t(mat),nrow=3,ncol=3)

print(trans)

row_vec <- c(1,2,3)
col_vec <- c(1,2,3)

col_mat <- matrix(mat[row_vec,col_vec]==trans[row_vec,col_vec],nrow = 3,ncol = 3)
print(col_mat[row_vec,col_vec])
vec1<-"TRUE"
for (i in 1:3) {
  for (j in 1:3) {
    if(col_mat[i,j]==FALSE){
      vec1<-"FALSE"
      break
    }
  }
}
if(vec1=="FALSE"){
  print("NOT SYMMETRIC")
}else{
  print("SYMMETRIC")
}

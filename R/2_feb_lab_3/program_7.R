M = matrix(c(1:16), nrow = 4,ncol = 4,byrow = TRUE)
print(M)

submat <- M[M[,3]>7,]
print(submat)
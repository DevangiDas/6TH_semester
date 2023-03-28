M = matrix(c(1:16), nrow = 4,ncol = 4,byrow = TRUE)
print(M)

row_vec <- c(1,2,3,4)
M[M[row_vec]<5,] <- 0
print(M)

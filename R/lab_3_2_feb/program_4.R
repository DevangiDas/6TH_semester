mat1 <- matrix(c(1:20),nrow = 5,ncol = 4)
print(mat1)

rows <- c("r1","r2","r3")
cols <- c("c1","c2","c3")
mat2 <- matrix(c(1:9),nrow = 3,ncol = 3,byrow = TRUE,dimnames = list(rows,cols))
print(mat2)

row <- c("r1","r2")
col <- c("c1","c2")
mat3 <- matrix(c(1:4),nrow = 2,ncol = 2,dimnames = list(row,col))
print(mat3)
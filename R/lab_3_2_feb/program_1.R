M <- matrix(3:14,nrow = 4)
print(M)

mymatrix1 <- matrix(3:14,nrow = 4,byrow = TRUE)
print(mymatrix1)

mymatrix2 <- matrix(3:14,nrow = 4)
print(mymatrix2)

rows = c("r1","r2","r3","r4")
columns = c("c1","c2","c3")
mymatrix3 <- matrix(3:14,nrow = 4,dimnames = list(rows,columns))
print(mymatrix3)

mymat <- mymatrix3[1,3]
print(mymat)

mymat1 <- mymatrix3[4,2]
print(mymat1)

mymat2 <- mymatrix3[2,]
print(mymat2)

mymat3 <- mymatrix3[,3]
print(mymat3)
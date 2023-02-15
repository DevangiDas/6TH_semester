mat = (3:14)
x <- matrix(mat,nrow=4)
print(x)

x2 <- matrix(mat,nrow = 4,byrow = TRUE)
print(x2)

x3 = matrix(mat,nrow = 4,bycol = TRUE)
print(x3)

rnames = c("r1","r2","r3","r4")
cnames = c("c1","c2","c3")
x4 <- matrix(mat,nrow = 4,dimnames = list(rnames,cnames))
print(x4)

x4[1,3]
x4[4,2]
x4[2,]
x4[,3]


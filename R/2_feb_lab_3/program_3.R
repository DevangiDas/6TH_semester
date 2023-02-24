vec1 <- c(2,4,6)
vec2 <- c(3,5,7)
mymat <- matrix(c(vec1,vec2),nrow=2,ncol = 3,byrow = TRUE)
print(mymat)

vec3 <- c(21,43,65)
vec4 <- c(36,52,72)
mymat1 <- matrix(c(vec3,vec4),nrow=2,ncol = 3,byrow = TRUE)
print(mymat1)

addmat <- mymat1 + mymat
print(addmat)

submat <- mymat1 - mymat
print(submat)

mulmat <- mymat1 * mymat
print(mulmat)

divmat <- mymat1 / mymat
print(divmat)
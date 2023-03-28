height <- 10  # Change this to set the height of the pyramid
for (i in 1:height) {
  for (j in 1:(height-i)) {
    cat(" ")
  }
  for (j in 1:(2*i-1)) {
    cat("*")
  }
  cat("\n")
}
n <- 4

# create matrix to store pattern
pattern <- matrix(" ", nrow = n, ncol = n*4-3)

# fill in matrix with appropriate characters
for (i in 1:n) {
  row_chars <- LETTERS[(i-1):(i*2-3)]
  row_chars <- c(rev(row_chars[-1]), row_chars)
  row_nums <- rep(i, ncol(pattern)-length(row_chars))
  pattern[i, ] <- c(rep(" ", n-i), row_nums, rep(" ", n-i-1), row_chars, rep(" ", n-i))
}

# print pattern
for (i in 1:n) {
  cat(paste0(pattern[i, ], "\n"))
}


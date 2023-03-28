input_str <- "abcdefghij"
for (i in seq(1, nchar(input_str), by = 2)) {
  char <- ""
  for (j in i) {
    char <- j
  }
  cat(char)
}
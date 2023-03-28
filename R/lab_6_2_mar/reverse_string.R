reverse_number <- function(num) {
  num_str <- as.character(num)
  rev_str <- ""
  for (i in seq(nchar(num_str))) {
    rev_str <- paste0(substr(num_str, i, i), rev_str)
  }
  return(as.numeric(rev_str))
}
num <- 12345
rev_num <- reverse_number(num)
cat("Original number:", num, "\n")
cat("Reversed number:", rev_num, "\n")
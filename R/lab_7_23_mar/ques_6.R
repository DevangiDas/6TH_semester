# Taking input string from user
input_string <- "DEVANGI DAS"

# Initializing an empty string to store the reversed string
reversed_string <- ""

# Reversing the input string
for (i in nchar(input_string):1) {
  reversed_string <- paste0(reversed_string, substr(input_string, i, i))
}

# Printing the reversed string
cat(paste0("The reversed string is: ", reversed_string, "\n"))

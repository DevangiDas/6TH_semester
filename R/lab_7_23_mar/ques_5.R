# Pre-defined string
string <- "DEVANGI DAS"

# Converting the string to lowercase
string <- tolower(string)

# Initializing a variable to count the number of vowels
vowel_count <- 0

# Counting the number of vowels
for (i in 1:nchar(string)) {
  if (substr(string, i, i) %in% c("a", "e", "i", "o", "u")) {
    vowel_count <- vowel_count + 1
  }
}

# Printing the number of vowels in the string
cat(paste0("The number of vowels in the string is: ", vowel_count, "\n"))

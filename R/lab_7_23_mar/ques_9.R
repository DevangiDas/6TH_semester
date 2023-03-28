# Function to replace multiple consecutive blanks with a single blank
replaceMultipleBlanks <- function(string) {
  # Replacing consecutive blanks with a single blank
  new_string <- gsub("\\s{2,}", " ", string)
  
  # Returning the modified string
  return(new_string)
}

# Example usage
input_string <-"Devangi    das"
output_string <- replaceMultipleBlanks(input_string)
cat(paste0("Input string: ", input_string, "\n"))
cat(paste0("Output string: ", output_string, "\n"))

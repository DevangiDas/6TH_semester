# Take user input for string, substring to search and string to insert
input_string <- readline("Enter a string: ")
sub_string <- readline("Enter a sub-string to search: ")
insert_string <- readline("Enter a string to insert: ")

# Find the position of the sub-string
position <- regexpr(sub_string, input_string)

# Insert the new string at the position of the sub-string
output_string <- paste0(substr(input_string, 1, position - 1), insert_string, substr(input_string, position + nchar(sub_string)))

# Print the output string
cat("The modified string is:\n", output_string)





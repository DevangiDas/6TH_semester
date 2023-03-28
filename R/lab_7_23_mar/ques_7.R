#Taking input string from user
input_string <- readline(prompt = "Enter a string: ")

#Extracting the 5-character sub-string
sub_string <- substr(input_string, start = 5, stop = 9)

#Replacing the sub-string with "V-Day"
new_string <- gsub(sub_string, "V-Day", input_string)

#Printing the modified string
cat(paste0("The modified string is: ", new_string, "\n"))

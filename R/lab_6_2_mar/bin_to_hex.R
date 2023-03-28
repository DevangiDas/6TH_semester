cat("Enter a binary number: ")                
binary_str <- readline()
cat("Enter the binary digits string: ")       
binary_digits <- readline()
cat("Enter the hexadecimal digits string: ")
hex_digits <- readline()
while (nchar(binary_str) %% 4 != 0) {     
  binary_str <- paste0("0", binary_str)
}
binary_groups <- strsplit(binary_str, "(?<=.{4})", perl = TRUE)[[1]]
hex_groups <- sapply(binary_groups, function(group) {                 
  decimal <- sum(as.numeric(strsplit(group, "")[[1]]) * 2^(3:0))    
  substr(hex_digits, decimal + 1, decimal + 1)                        
})
hex_str <- paste0(hex_groups, collapse = "")
cat("Binary number:", binary_str, "\n")
cat("Hexadecimal number:", hex_str, "\n")



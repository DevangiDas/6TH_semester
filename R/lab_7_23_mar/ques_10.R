# Prompt the user for the month and year
month <- as.integer(readline("Enter month (1-12): "))
year <- as.integer(readline("Enter year: "))

# Get the number of days in the specified month and year
num_days <- as.integer(format(as.Date(paste(year, month, "1", sep="-")), "%d"))

# Get the day of the week of the first day of the month
first_day <- as.integer(format(as.Date(paste(year, month, "1", sep="-")), "%u"))

# Print the calendar header
cat(paste(month.name[month], year, "\n"))
cat("Mo Tu We Th Fr Sa Su\n")

# Print the calendar body
day_counter <- 1
for (i in 1:6) {
  for (j in 1:7) {
    if (i == 1 && j < first_day) {
      # Print blank space for days before the first day of the month
      cat("    ")
    } else if (day_counter > num_days) {
      # Print blank space for days after the last day of the month
      cat("    ")
    } else {
      # Print the day of the month
      cat(sprintf("%2d  ", day_counter))
      day_counter <- day_counter + 1
    }
  }
  # Move to the next line
  cat("\n")
  if (day_counter > num_days) {
    # All days have been printed, exit the loop
    break
  }
}
 
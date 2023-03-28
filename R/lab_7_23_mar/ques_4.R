# Create a data frame of student information
students <- data.frame(
  roll_num = c(1, 2, 3, 4, 5),
  name = c("Alice", "Bob", "Charlie", "David", "Eve"),
  department = c("CS", "ECE", "ME", "CS", "ME"),
  course = c("B.Tech", "B.Tech", "B.Tech", "M.Tech", "M.Tech"),
  join_year = c(2019, 2020, 2019, 2021, 2020)
)

# Define a function to print names of students who joined in a particular year
print_students_by_year <- function(df, year) {
  names <- df$name[df$join_year == year]
  if (length(names) == 0) {
    message("No students joined in ", year)
  } else {
    message("Students who joined in ", year, ":")
    for (name in names) {
      message(name)
    }
  }
}

# Define a function to print the data of a student given their roll number
print_student_by_roll_num <- function(df, roll_num){
  row <- df[df$roll_num == roll_num, ]
  if(nrow(row) == 0
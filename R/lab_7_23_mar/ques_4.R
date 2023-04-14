print_students_by_year <- function(df, year) {
  names <- df$Name[df$Year_of_joining == year]
  if (length(names) == 0) {
    cat("No students joined in the year", year, "\n")
  } else {
    cat("Students who joined in the year", year, ":\n")
    cat(names, "\n")
  }
}

# function to print names of students who joined in a particular year
students_by_year <- function(year) {
  names <- students[students$join_year == year, "name"]
  if (length(names) == 0) {
    cat("No students joined in the year", year, "\n")
  } else {
    cat("Students who joined in the year", year, ":\n")
    for (name in names) {
      cat(name, "\n")
    }
  }
}

# function to print data of student by roll number
student_by_roll_num <- function(num) {
  student_data <- students[students$roll_num == num, ]
  if (nrow(student_data) == 0) {
    cat("No student found with roll number", num, "\n")
  } else {
    cat("Data for student with roll number", num, ":\n")
    print(student_data)
  }
}

# function to print names of students who joined in a particular year
students_by_year <- function(year) {
  names <- students[students$join_year == year, "name"]
  if (length(names) == 0) {
    cat("No students joined in the year", year, "\n")
  } else {
    cat("Students who joined in the year", year, ":\n")
    for (name in names) {
      cat(name, "\n")
    }
  }
}

# function to print data of student by roll number
student_by_roll_num <- function(num) {
  student_data <- students[students$roll_num == num, ]
  if (nrow(student_data) == 0) {
    cat("No student found with roll number", num, "\n")
  } else {
    cat("Data for student with roll number", num, ":\n")
    print(student_data)
  }
}

students_df <- data.frame(
  roll_number = c(101, 102, 103, 104, 105),
  name = c("John", "Jane", "Tom", "Mary", "David"),
  department = c("Computer Science", "Mathematics", "Physics", "Chemistry", "Biology"),
  course = c("B.Tech", "B.Sc", "M.Sc", "Ph.D", "B.Sc"),
  year_of_joining = c(2018, 2019, 2020, 2017, 2021)
)

print_students_by_year(df, 2020)

print(students_df)

students_by_year(2020)
student_by_roll_num(103)
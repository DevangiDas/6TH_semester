# Create a vector of pet types
pet_types <- c("dog", "cat", "hamster", "goldfish")

# Set the number of pets to generate
num_pets <- 1000

# Generate a vector of randomly selected pets
pets <- sample(pet_types, num_pets, replace = TRUE)

# Display the first few pets
print(head(pets))

# Count the number of each type of pet
print(table(pets))
# Load the beaver data sets
data(beaver1)
data(beaver2)

# Add an "id" column to each data set
beaver1_with_id <- cbind(beaver1, id = 1)
beaver2_with_id <- cbind(beaver2, id = 2)

# Combine the two data sets into a single data frame
print(beaver_data <- rbind(beaver1_with_id, beaver2_with_id))

# Select the subset where body temperature is above 10
print(high_temp_beavers <- subset(beaver_data, Tb > 10))

# View the resulting data set
print(high_temp_beavers)
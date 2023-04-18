# Write your code here
cars = ('coupe', 'coupe', 'coupe', 'carbiolet', 'sedan')

# Count the number of times the 'coupe' element appears in the tuple
fav = cars.count('coupe')

# Calculate the length of the tuple
amt = len(cars)

# Calculate the percentage of coupes in the tuple
percentage = fav / amt

# Check if the percentage of coupes is more than 45%
if percentage > 0.45:
    print("Too many coupes in the garage.")
else:
    print("You are all set with cars.")

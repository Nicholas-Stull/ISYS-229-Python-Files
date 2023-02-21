#imports sys function to read command-line arguments that have been passed to the interpreter

# Import the sys module
import sys

# Get the user's birth year
year_born = int(input("Enter the year you were born: "))

# Calculate the approximate age based on the birth year and the current year
age_difference = 2023 - year_born

# Print the user's first name, which is passed as the first argument to the script
print("Your first name is: ", sys.argv[1])

# Print the user's middle initial, which is passed as the second argument to the script
print("Your middle initial is: ", sys.argv[2])

# Print the user's last name, which is passed as the third argument to the script
print("Your last name is: ", sys.argv[3])

# Print the user's approximate age
print("You are approximately", age_difference, "years old")

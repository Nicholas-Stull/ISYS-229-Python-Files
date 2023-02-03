#imports sys function to read command-line arguments that have been passed to the interpreter

import sys

year_born = int(input("Enter the year you were born: "))
age_difference = 2023 - year_born #calculates approximate age

print("Your first name is: ", sys.argv[1])
print("Your middle initial is: ", sys.argv[2])
print("Your last name is: ", sys.argv[3])
print("You are approximately", age_difference, "years old")

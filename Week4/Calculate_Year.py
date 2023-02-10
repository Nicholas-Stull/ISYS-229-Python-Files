# Import the date module from the datetime library
from datetime import date

# Get the user's birth year
Birthdateyear = int(input("Enter your birth year: "))

# Get the user's birth month
Bithdatemonth = int(input("Enter your birth month: "))

# Get the user's birth day
BirthdateDay = int(input("Enter your birth day: "))

# Get the current date
today = date.today()

# Calculate the user's age based on their birth date and the current date
age = today.year - Birthdateyear - \
    ((today.month, today.day) < (Bithdatemonth, BirthdateDay))

# Print the user's age in years
print((age), "years")

# Python3 code to calculate age in years

from datetime import date
Birthdateyear = int(input("Enter your birth year: "))
Bithdatemonth = int(input("Enter your birth month: "))
BirthdateDay = int(input("Enter your birth day: "))

today = date.today()
age = today.year - Birthdateyear - ((today.month, today.day) < (Bithdatemonth, BirthdateDay))
print((age), "years")
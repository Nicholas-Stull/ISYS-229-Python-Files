# importing date class from datetime module
from datetime import date

# creating the date object of today's date and legal age requirement
todays_date = date.today()
legal_age = 35

#collecting user input
first_Name = input("What is your first name? ")
last_Name = input("What is your last name? ")
userAge = input("And how old are you? ")

#Create a function
def age_calc(userAge):
		age_diff = legal_age - int(userAge)
		return age_diff

#printing user information ensuring to capitalize user's first name
print(f"Your name is {first_Name.capitalize()} {last_Name.capitalize()}, and your current age is {userAge}")

#if statement to print outcomes based on user input
if int(userAge) >= legal_age:
	print("You are old enough to run for president. ")
else:
    #Call to number of years to wait function
	Num_of_years = age_calc(userAge)
	print(f"Wait until you turn {legal_age} years of age to run for the office of President. Which should be in about {Num_of_years} years from {todays_date}!")
	
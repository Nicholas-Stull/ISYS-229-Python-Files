# import date class from datetime module
from datetime import date


# create the date object of today's date and legal age requirement variable

# today() to get current date
todays_date = date.today()

print("Today's date =", todays_date)

#current_year = date.today().year
#year_of_birth = int(input('Enter Year Of Birth: '))
#age = current_year - year_of_birth
#print('You are %s years old.' % age)
#if age < 18:
#    print('YOU SHALL NOT PASS!')
#else:
#    print('Welcome To The Portal.')



#collecting user input regarding their first and last name along with their current age
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

#create a function that calculates the difference between legal age and current age and then returns a value
legal_age = 21
age_gap = int(legal_age - age)
#print (f_name, "you are" , age, "years old.", "you are" , age_gap, "years away from being able to drink legally.")

#print user information ensuring to capitalize user's first and last name using the f function. The user's age should also be printed on the same sentence
print("Hello", f"{f_name.capitalize()} {l_name.capitalize()}"",","you are", age, "years old.","You are", age_gap, "years away from being able to drink legally.")

#Develop an if statement to determine if the user is too young to run for president
president_age = 35
president_age_gap = int(president_age - age)
#If the user is old enough, you should print a statement that states "You are old enough to run for president"
if age >= president_age:
    print("You are old enough to run for president.")
else:
    print("Wait until you turn", president_age, "years old to run for the office of President. Which should be in about", president_age_gap, "years from", todays_date)
#If the user is not old enough, you should develop an else statement that calls a function to determine the age gap and then print the following
#Wait until you turn (legal age variable) years old to run for the office of President. Which should be in about (function variable) years from (today's date variable)


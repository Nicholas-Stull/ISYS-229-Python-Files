space = " "
fname = input("Please enter your first name:") #fname() is a function that takes the first name from the user using the input() function
lname=("Please enter your last name:") #lname() is a function that takes the last name from the user using the input() function
age = int(input("Please enter your age:") #age() is a function that takes the age from the user using the input() function and uses the int() function to convert the input to an integer
lbs=int(input("Please enter your weight in pounds")) #lbs() is a function that takes the weight from the user using the input() function and uses the int() function to convert the input to an integer
ft=int(input("Please enter your height in feet"))
kg,ounces,m = lbs * 0.045, lbs * 16, ft * 0.3048 #kg,ounces,m are variables that take the inputed value and turn it into kilograms, ounces, and meters
if m <= 1: #if the user is less than or equal to 1 meter tall, the program will print the following
    print("Thank you," + space + fname + space + lname + "." + space + "You are" + space + str(age) + "." + " You weigh" + space + str(kg) + space + "Kilograms, or" + space + str(ounces) + space + "ounces." + space + "You are" + space + str(m) + space + "meter tall.")
else: #if the user is more than 1 meter tall, the program will print the following
    print("Thank you," + space + fname + space + lname + "." + space + "You are" + space + str(age) + "." + " You weigh" + space + str(kg) + space + "Kilograms, or" + space + str(ounces) + space + "ounces." + space + "You are" + space + str(m) + space + "meters tall.")

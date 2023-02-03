space = " "
print("Please enter your first name")
fname = input()
print("Please enter your last name")
lname = input()
print("Please enter your age")
age = int(input())
print("Please enter your Weight")
lbs = int(input())
print("Please enter your height in feet")
ft = int(input())
kg = lbs * 0.045
ounces = lbs * 16
m = ft * 0.3048
if m <= 1:
    print("Thank you," + space + fname + space + lname + "." + space + "You are" + space + str(age) + "." + " You weigh" + space + str(kg) + space + "Kilograms, or" + space + str(ounces) + space + "ounces." + space + "You are" + space + str(m) + space + "meter tall.")
else:
    print("Thank you," + space + fname + space + lname + "." + space + "You are" + space + str(age) + "." + " You weigh" + space + str(kg) + space + "Kilograms, or" + space + str(ounces) + space + "ounces." + space + "You are" + space + str(m) + space + "meters tall.")

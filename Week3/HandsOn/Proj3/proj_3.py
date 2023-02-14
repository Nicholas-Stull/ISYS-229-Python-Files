print("Please input you first name")
fname = input()
print("Please input you last name")
lname = input()
print("Please input you age")
age = float(input())
yes = "with running for president since you are"
no = "you are a too young to run for president since you are"
if age >= 35:
    print("Good luck " + fname + lname + yes + str(age))
else:
    print("Good luck" +fname + lname + no + str(age))

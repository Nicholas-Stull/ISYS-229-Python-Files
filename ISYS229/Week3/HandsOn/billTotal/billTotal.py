print("Please enter the amount of the bill.")
bill = float(input())
if bill < 25:
    tip = bill * 0.15
else:
    tip = bill * 0.2
total = bill + tip
print("Your total bill including tip is $" + str(total))

# Week 1 Python

## drinking.py

The [drinking.py](ISYS-229-Python-Files/blob/master/Week1/drinking.py) script is a simple program that prompts the user for their name and age, and then checks their age to determine whether or not they can drink. If the user is over 21 years old, the program prints "Let's go drink!". If the user is between 18 and 21, it prints "Can't Drink today, head over to Canada". If the user is less than 18 years old, it prints "Not Today". The program also includes messages advising against drinking and driving. The `sleep()` function is used to pause the program for one second before printing the messages.

## vote_eligibility.py

The [drinking.py](ISYS-229-Python-Files/blob/master/Week1/voting.py) script is a simple program that prompts the user for their name and age, and then checks their age to determine whether or not they are eligible to vote in the United States. If the user is 18 years of age or older, the program prints "You are old enough to vote in the U.S.". If the user is under 18 years of age, the program prints "Wait until you turn 18 years of age before you can vote in the U.S.".

Both of these scripts are simple examples of Python programs that use conditional statements to make decisions based on user input. They demonstrate the basic syntax for working with `if-else` statements and input functions in Python.

## [Python Code from Class](ISYS-229-Python-Files/blob/master/Week1/Samples/sample1.py) 
```python
userName = input("what is your name? ")
userAge = input("And how old are you? ")

print("Hello " + userName)

if int(userAge) >= 18:
	print("You are old enough to vote in the U.S.")
else:
	print("Wait until you turn 18 years of age before you can vote in the U.S.")
```
# Lesson 7.1

##  A First Look at OOP

1.       Object-oriented programming (OOP): Programming paradigm based on concept of objects.

1.       Objects: Capsules of properties and procedures/methods.

2.       Allows us to abstract actual code and think more about attributes of data and operations around data.

3.       Advantages:

1.       Code reusable.

2.       Easier to design software as you can model it in terms of real-world objects.

3.       Easier to test, debug, and maintain.

4.       Data is secure due to abstraction and data hiding.

# Lesson 7.2

## OOP in Python

1.       Classes are OOP building-blocks.

1.       Blueprints for objects.

2.       Everything in Python is an object.

3.       Running type function on any object will reveal class.

# Lesson 7.2.1

## Defining a Class in Python

1.       Syntax is minimal.

1)      class ClassName

2)      type function shows class type.

3)      In Python, class and type are synonymous.

2.       Class: blueprint

3.       Attributes: noun, parts of the object

4.       Methods: action, things the object does

5.       Instantiation: copies of the class

6.       Declaring the Employee Class

```python 
```class Employee:
def _ _ init _ _(self, fname, lname, age):
	self.fname = fname
	self.lname = lname
	self.age = age
def fullname (self):
print(f”Hello {self.fname} {self.lname}, you are {self.age} years old.”)
emp_1 = Employee(‘Eric’, ‘Clayborn’, 23) emp_1.fullname()
emp_2 = Employee(‘Andrew’, ‘Churchill’, 25) emp_2.fullname()
```

7.       Developing the Attributes (nouns)

1)      Each method within a class automatically takes the instance as the first argument.

2)      Always call it “self”

3)      Create method containing self using a print statement to display full name and age

4)      Call the methods in order to display the actions or results

5)      Notice the ( ) located at the end, because it is a method being called rather than an attribute being passed

6)      This displays the return value of the method
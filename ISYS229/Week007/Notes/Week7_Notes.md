# Week 7: Notes
## Lesson 4.1: Types of Functions
1. A group of statements within a program that performs a specific task
2. Allows you to reuse code
3. Two types of functions
    1. Built-in functions
    2. User-defined functions
4. Can be used anywhere in your code without importation.
5. Python has many.

Examples:
```python
input([prompt]): takes input from user
print(): displays output
```

## <mark style="background-color: #FFFF00">Lesson 4.2: User-Defined Functions </mark>
1. Functions written by user.
2. Helps organize program into logical fragments.
3. Allows reuse of code.
4. Use following steps to define function:
    1. Use defkeyword followed by function name.
    2. Add parameters within parentheses. End definition with colon.
        - <mark style="background-color: #FFFF00">Parameters are information that needs to be passed to function for it to work.</mark>
        - Optional
    3. Write logic.
    4. Use returnkeyword to return output. If not used, Noneis returned.
5. Syntax is shown in Snippet 4.3.

Syntax:
```python
def function_name(parameter_one, parameter_two, parameter_n):
    # logic
    return output
```
Example:
```python
def add_numbers(num_one, num_two):
    return num_one + num_two
```
### Steps to Call a Function
Step 1: Declare a function
```python
def sum(arg1, arg2):
    print(arg1 + arg2)
```
Step 2: Call a function
```python
sum(15, 60)
sum(‘Hello’, ‘World’)
sum(15.4, 4.6)
sum(‘Hello’, 15)
```
Output:
```terminal
    75
    HelloWorld
    20.0
    type error
```

## Lesson 4.2.1: Calling a Function
1. Can call functions at interactive prompt or from within some other part of your code.
2. Names of arguments passed do not need to match parameter names.
3. Number of arguments should match number of parameters.

Example:
This function provides a call, but no return
- Parameter --> val
- Argument --> ()
```python
def myfunc(val):
    print(“Hello ” + val)
myfunc(“ ”)
myfunc(“Python”)
myfunc(“Ruby”)
myfunc(“Java”)
```
Output:
```terminal
    Hello
    Hello Python
    Hello Ruby
    Hello Java
```
 
## Lesson 4.2.2: Global and Local Variables
1. <mark style="background-color: #FFFF00">Local variables: variables defined inside body of function. </mark>
    -  <mark style="background-color: #FFFF00">Have local scope. </mark>
        - <mark style="background-color: #FFFF00"> Only available within function it is defined. </mark>
2. <mark style="background-color: #FFFF00"> Global variables: variables defined outside of function body. </mark>
    - <mark style="background-color: #FFFF00">Have global scope. </mark>
        - <mark style="background-color: #FFFF00">Available both outside and inside of functions. </mark>

Example:
```python
def myfunc():
X = 10; #this is an example of a local scope
Y = 20; #this is an example of a global scope
```

## Lesson 4.2.3: Function Return
1. ```return``` <mark style="background-color: #FFFF00">statement is used to return something to caller of function. </mark>
2. Not necessary for functions that do not need to return a value.
3. If not used, function returns ```None```.

Example
- This function provides a call and returns a value
1. <mark style="background-color: #00FF00">Parameter</mark> - > ```Val```
2. <mark style="background-color: #964B00">Argument</mark> - > ```15```
```python
def myfunc(val):
    return val* 2
print(myfunc(15))
```
Output:
```terminal
    30
```

1. Arguments are actual values or references assigned to parameters at runtime.
2. Python supports several types or arguments:
	1. Required arguments
	2. Keyword arguments
	3. Default arguments
	4. A variable number of arguments

## Lesson 4.3.1: Required Arguments

1. Have to be present when calling function.
2. Need to be in correct order. 
<mark style="background-color: #9AFDFF">False Example:</mark>
```python
def division(first, second):
	return first/second
	value = division(10)
	print(value)
	```
Output
```Terminal
>> TypeError: missing 1 required positional argument
```


<mark style="background-color: #9AFDFF">Correct Example:</mark>
```python
def division(first, second):
	return first/second
	value = division(10, 5) 
	print(value) 
```
Output:
```terminal
>> 2.0
```

### Lesson 4.3.2: Keyword Arguments
1. Identify arguments by parameter names.
Example function call: 
 ```python
quotient = division(second=2, first=10)
```
2. Ensures arguments are passed to correct parameters, no matter the order.
Example:
```python
def my_bill(tiprate, tax, subtotal):
	return (subtotal * tax) + (subtotal * tiprate) 
total = my_bill(subtotal=20, tiprate=0.15, tax=1.06 )
	print(round(total, 2))
```
Output
```terminal
>> 24.2
```

## Lesson 4.3.3: Default Arguments
1. Takes default value if no argument is passed during function call.
<mark style="background-color: #FFFF00">Example function definition:</mark>
```Python
def division(first, second=2):
```
2. <mark style="background-color: #FFFF00">Can pass an argument to override default value.</mark>
```python 
def division(first, second=2):
	return first/second 
Quotient = division(10)
```
3. Takes default value if no argument is passed during function call.
Example function definition:
```python
def division(first, second=2):
```
Example1
```python
def multiple_display(message = ‘default’, times = 2):
	for x in rage(times):
		print(message)

multiple_display()
```
Output
```terminal
>> default
>> default
```

Example2
```Python
def multiple_display(message = ‘default’, times = 2):
	for x in rage(times):
		print(message) 
		
multiple_display(‘roadrunner’, 3)
```
Output
```terminal
>> roadrunner
>> roadrunner
>> roadrunner
```

## Lesson 4.3.4: Variable Number of Arguments
1. Python allows variable number of arguments with * syntax.
Example function definition:
```python
def print_arguments(*args):
```
2. Can use loop to iterate over arguments. 
	1. Creates a tuple
Example
```python
def student(name, age, *otherinfo): 
	print("name: ", name) 
	print('age: ', age ) 
	#print('other information: ', otherinfo) 
	for x in otherinfo:
		if type(x) == bool:
			continue 
		print(x)
student('Eric', 19, "Python", False, "Instructor", 23.6)
```

## Lesson 4.4: Anonymous Functions
1.  <mark style="background-color: #FFFF00">Anonymous funcations are also called lambda functions.</mark>
2. Does not need to be named in definition.
3. Usually throwaway functions.
	1. Not called in other parts of code.
Syntax: 
```syntax
lambda argument_list: expression
```
4. Usually used in combination with ```map()```, ```reduce()```, and ```filter()``` functions.

| Generally defined functions     | Lambda functions             |
|---------------------------------|------------------------------|
| def myfunc(val): return val * 2 | myfunc = lambda val: val * 2 |
| print(myfunc(15))               | print(myfunc(15))            |

## Summary
In this module:
1. We learned about the various types of functions in Python, as well as their differences, syntax, and use cases. 
2. We covered how and where to apply the different types of functions, and how they can be used to help break your programs into smaller subprograms that achieve a specific purpose.
3. We also saw how the use of functions can help reuse functionality in our code and avoid repeating the same blocks of code.
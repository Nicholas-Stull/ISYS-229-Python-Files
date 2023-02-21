# Module 1 : Introduction to Python
## Lesson 1.1:
### Working with the Python Interactive Shell
1. Python Interactive Shell:
    1. Open at command line using command: python
    2. Interfaces with Python interpreter.
    3. Allows user to run Python commands at command line.
    4. Sample command: ```print("Message")```
    5. Anything typed into shell is echoed back.• Can even do calculations.

Example:

Simple Print Statement 
```python 
print(“Happy Birthday”)
```
Print Calculations

```python
print(5 * 4)
print(24 + 6 * 3)
```

Print whole numbers using commas to separate

```python
print(0,1,2,3,4)
```
Repeat Strings
```python
print(“- - - - -”)
print(“-” * 5)
print(“hello   “ * 5)
```

## Lesson 1.2
###Writing and Running Simple Scripts
1. Can also run code saved in file.
    2.These files are called modules.
    3.A script is a module that is run from the command line.
    4. To run a script, type the following at the command line:
        1. python scriptname.py
        2. Example: python hello.py
    5. To run a script, you must be in the same directory as the script.
    6. To run a script, you must have the correct permissions.

## Lesson 1.2.1 
### Running a File Containing Invalid Commands
1. Invalid commands in script will cause errors
2. Output will be stack trace (also called traceback)
    1. Gives error message and line number where error occurred.
    2. Can be used to find and fix errors in code.
    3. Reads from bottom up.
    EXAMPLE:
    ```python
    print(invalid instruction)

### Passing User Argument to Scipts
1.  To Pass arguments to scripts, use the sys module. 
   ```python
   import sys
   print(sys.argv)
   ```
2. The sys function allows users to read command-line arguments that have been passed to the interpreter.
3. The sys.argv list contains the argument(s) passed to the script.
    1. Can pass any # of argument(s) to script.
    2. First argument is always the name of the script. Example: ```sys.argv[0]```
    3. Second argument is the first argument passed to the script. Example: ```sys.argv[1]```

Example Print Statement:
```python
import sys
print("First Name: ", sys.argv[1])
print("Middle Name: ", sys.argv[2])
print("Last Name: ", sys.argv[3])
```
Example Output:
```python
python name.py John Paul Smith
First Name: John
Middle Name: Paul
Last Name: Smith
```

## Lesson 1.3
### Variables
1. Variables can reference values of different data types.
    1. <mark >They refer to values in memory<mark >
2. They don’t need to be declared before use.
    1. ```X = “No need to declare this string before use”```
3. Value and ```type``` can change during runtime.
4. Use type function to check type. 
    Example: ```type(X)```

### Naming Identifiers and Reserved Words
1. Some rules for variables and other identifiers:
    1. Can consist of upper and lowercase letters, underscores, unicode identifiers, and digits 0 to 9.
    2. Cannot begin with digit.
    3. No other characters can be in identifiers.
        1. Module names with spaces should be avoided.
    4. Python reserved words or keywords can’t be used
2. Identifier names are case sensitive

### Python Naming Conventions
### These are guidelines only
1.  Compound variable names should be written in snake case notation.
*  Example: ```snake_case```
2. Avoid using the following• Example: PascalCase
*   Example: ```camelCase```
3. Constant names should be in all caps.

4. Avoid lowercase L / uppercase O as single character names.

### Data Type Variables
1. Python has 5 data types:
    1. Integer
        1. Whole numbers (Numeric Values)
        2. Can be positive or negative
        3. Arithmetic operations can be performed on integers
    2. Float
        1. Decimal numbers (Numeric Values)
        2. Can be positive or negative
        3. Arithmetic operations can be performed on floats
    3. String
        1. Sequence of characters between quotes
        2. Can be single or double quotes
        3. Can contain letter,#'s or symbols
    4. Boolean
        1. True or False
        2. Used in conditional statements
    5. None
        1. Represents nothing
        2. Used in conditional statements

### Conversion Between Data Types
1. Can convert between data types using the following functions:
    1. int()
    2. float()
    3. str()
    4. bool()
    5. None

### Assigning Values to Variables
1. Can assign values to variables using the assignment operator ( = ).
    1. Example: ```X = 5```
2. Can assign multiple values to multiple variables in a single line.
    1. Example: ```X, Y, Z = 1, 2, 3```
3. Error is raised if number of variables on left side of assignment operator does not match number of values on right side.
    1. Example: ```X, Y, Z = 1, 2``` will raise an error.

#### Example1
Simple Print statement to conceatrate string values
```python
print("I Love Python + " "I Love Programming")
print("I Love Python" + " " + "I Love Programming")
```
or

```python
message = "I Love Python"
print(message + " " + "I Love Programming")
print( message , "!" *3 ")
```
#### Example2
Multiple Assignment
```python
a , b ,c = 1 , 2 , 3
print(a)
print(b)
print(c)

or 

print(a,b,c)
```

## Lesson 1.4
### User Input, Comments, and Indentations

1. User Input from the Keyboard
2. Use input() function to get user input from keyboard.
    1. Example: ```message = input()```
3. Program execution halts until user inputs value and presses Enter key.
4. Passing in a Prompt to the Input Function
    1. Syntax: ```input("Insert prompt here")```
5. Using Different Input Data Types in Your Program
6. The input() function always returns string.
7. Use built-in int() function to convert to integer

#### Example1
```python
age = input("Enter your age: ")
print("You are " + age + " years old.")
```
#### Example2
```python
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")
```

### Comments
Block
1. Start with # sign.
2. Comes on line before statement it annotates.
3. Placed at same indent level as statement.
Inline
1. Start with # sign.
2. Placed on same line as statement it annotates.
Documentation String (docstrings)
1. String wrapped in triple (double or single) quotation marks.
2. Module docstrings should be at beginning of file.
3. Can be used for multiple line comments.

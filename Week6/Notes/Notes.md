# Lesson 3.1.1 - 3.9.3
## Lesson 3.1.1 - Program Flow
1. Describes the way in which statements are executed in a program.
2. Python has a top-down program flow.

## Lesson 3.1.2 - Control Statements
1. Control statements are used to control the flow of a program.
2. The two main control statements are:
    1. ```if```
    2. ```while```

## Lesson 3.2 - if Statement
1. The ```If``` statement allows execution of block of code if condition is true, otherwise it can run block in else clause. 
    1. ```else``` is optional.
    2. ```else if``` is abbreviated as ```elif```
2. Can chain multiple ```if``` statements together.

Example:
```python
if condition1:
    # do something
elif condition2:
    # do something else
else:
    # do something else
```
## Lesson 3.3 - while Statement
1. The ```while``` statement allows execution of block of code while condition is true.
2. Can chain multiple ```while``` statements together.
3. Allows execution of block of code repeatedly until condition is false.
    1. else clause is optional.
4. Can Also have ```else``` clause.
    1. This will be executed exactly once when the condition becomes false.

Example:
```python  
while condition:
    # do something
else:
    # do something else
```
## Lesson 3.4 - While vs If
1. ```if``` gives opportunity to branch execution of code based on condition.
2. ```while``` gives opportunity to run block of code multiple times as long as condition is true.
    1. Can be considered a loop.
Example:
```python
if condition:
    # do something
else:
    # do something else
```
Example:
```python
while condition:
    # do something
else:
    # do something else
```

## Lesson 3.5 - Loops
1. Way to execute a block of code multiple times.
2. Used to iterate (or Loop ) over iterables
3. Iterables are objects that can be iterated over.
    1. Strings, Lists, Tuples, Dictionaries, Sets, and Files are all iterables.
Example:
```python
for item in iterable:
    # do something
```
## Lesson 3.6 - The for Loop
1. The ```for``` loop is used to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
2. Also referred to as the ```for in``` loop.
3. Used when you want to repeatedly execute a block of code a number of times.
4. Runs a predetermined number of times.
    1. While loops run until a condition is met.

Example:
```python
for item in iterable:
    # do something
```
## Lesson 3.6.1 - Using else
1. ```else``` statement can be used with ```for``` loops.
2. Will execute once when exits cleanly
3. useful of debugging
Example:
```python
for item in iterable:
    # do something
else:
    # do something else
```

## Lesson 3.7 - The range() Function
1. The ```range()``` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
2. Can be used to iterate over a sequence of numbers.
syntax:
```python
range([start], stop, [step])
```
- start: starting number of the sequence.
- stop: generate numbers up to, but not including this number.
- step: difference between each number in the sequence.

Example:
```python
for i in range(10):
    print(i)
```
Example:
```python
for a in range(1,4):  #creates a range of numbers starting at 1 end at 4
for b in range(a): #selects values from range variable a
print(“*”, end=‘ ’) #prints the * based on the value, end returns a new line
print()******
```
## Lesson 3.8: Nesting Loops
1. Practice of placing loops inside other loops.
2. Important to use for accessing data inside complex data structures.
3. No limit to how far you can nest.

Example:
```python
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=’\t’)
    print()
```
## Lesson 3.9.1: The break Statement
1. The ```break``` statement allows you to exit loop based on external trigger.
2. The break statement allows you to exit loop based on external trigger.
3. Usually used in conjunction with if statement.
4. The break statement allows you to exit loop based on external trigger.
5. Usually used in conjunction with if statement

Example:
```python
for value in “Python”: #the variable called value is passed the string Python
    if value == “t”: #the if statement is used to search the string for a value of t
        break #if the loop control variable identifies the letter t, it breaks from the execution
    print(value); #prints the indexes within the value variable 
```
    >>> P
    >>> y
## Lesson 3.9.2: The continue Statement
1. The continue statement allows you to skip over part of loop where external condition is triggered, but goes back to top of loop and continues execution.
2. Usually used in conjunction with ```if``` statement.
3. The continue statement allows you to skip over part of loop where external condition is triggered, but goes back to top of loop and continues execution.
4. Usually used in conjunction with ```if``` statement.
Example:
```python
for value in “Python”: #the variable called value is passed the string Python
    if value == “t”: #the if statement is used to search the string for a value of t
        continue #if the loop control variable identifies the letter t, it continues from the execution
    print(value); #prints the indexes within the value variable 
```

## Lesson 3.9.3: The pass Statement
1. The ```pass``` statement is a null operation; nothing happens when it executes.
2. Allows you to handle an external trigger condition without affecting the 
execution of the loop
3. The ```pass``` statement is a null operation; nothing happens when it executes.
Example:
```python
for value in “Python”: #the variable called value is passed the string Python
    if value == “t”: #the if statement is used to search the string for a value of t
        pass #if the loop control variable identifies the letter t, it passes from the execution
    print(value); #prints the indexes within the value variable 
```










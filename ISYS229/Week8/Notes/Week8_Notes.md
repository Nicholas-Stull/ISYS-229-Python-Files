# Module 5 
## Lists and Tuples

1. List
	1. Data structure that holds ordered collections of related data. 
	2. Known as arrays in other languages.
	3. Properties:
		1. Are ordered: items have a defined order, and that order will not change
		2. If you add new items to a list, the new items will be placed at the end of the list.
		3. Contain objects of arbitrary types.
		4. Elements can be accessed by index.
		5. Are arbitrarily nestable.
		6. Have variable sizes.
		7. Are mutable: we can change, add, and remove items in a list after it has been created.
2. Tuple
	1. Holds together multiple related objects.
	2. Are immutable.

# Lesson 5.1
## List Syntax
```python
# Empty list 
[]

#list containing numbers
[2,4,6,8,10]

#list with mixed types
["one",2,"three", ["five",6]]
```

# Lesson 5.2.1
## list.append(item)
1. Adds single item to end of list. 
	1. Doesn’t return new list; modifies original.
```bash
>>> things = ["first"]
>>> things.append("another thing")
>>> things
['first','another thing']
```

# Lesson 5.2.2
## list.extend(iterable)
1. Extends list by appending all items in iterable to end of list. 
	1. If string is passed, each character is appended to list.

# Lesson 5.2.3
## list.insert(index, item)
1. Inserts item at given index.
	1. Both arguments are required.
```bash
>>> things=["second"]
>>> things.insert(0,"first")
>>> print(things)
['first','second']
```

# Lesson 5.2.4
## list.remove(item)
1. Removes first item whose value matches the passed argument item.
```bash
>>> things = ["first", "second"]
>>> things
['first','second']
>>> things.remove("second")
>>> things
['first']
```

# Lesson 5.2.5
## list.pop([index])
1. Removes item at given index and returns it.
	1. Index argument is optional. If not specified, last item is removed.
```bash
>>> things =  ["first","second","third"]
>>> things
['first','second','third']
>>> second_item = things.pop(1)
>>> second_item
'second'
>>> things
['first','third']
 ```
 
# Lesson 5.2.6
## list.clear()
1. Removes all items from list. 
	1. Alternate: del list[:]
	```python
fruits = ["apple","bananna","cherry"]
fruits.clear()
print(fruits)
```

# Lesson 5.2.7
## list.index(item [, start [, end]])
1. Returns index of first item in list whose value is item. 
	1. start and end are optional; searches entire list if not provided.
``` python
fruits = [4,55,64,32,16]
x = fruits.index(32)
print(x)
```
```bash
>>> 3
```

```python
fruits = ['apple','bananna','cherry']
x = fruits.index("cherry")
print(x)
```
```bash
>>> 2
```

# Lesson 5.2.8
## list.count(item)

1. Returns number of times given item occurs in list.
```python 
fruits = ['cherry','apple','bananna','cherry','apple','bananna']
x = fruits.count("cherry")
print(x)
```
```bash
>>> 3
```

# Lesson 5.2.9
## list.sort(key=None, reverse=False)
1. Sorts list items.
	1. key and reverse are optional.
	2. key specifies function to be called on each item prior to comparison.
		1. Useful if you have list of lists and want to sort on element of sublist. 
	3. reverse specifies sort order.
		1. False sorts in ascending. 
		2. True sorts in descending.

# Lesson 5.2.10
## list.reverse()
1. Reverses element in list.
```python
fruits = ['apple','banana','cherry']
fruits.reverse()
print(fruit)
```
```bash
>>> ['cherry','banana','apple']
```

# Lesson 5.3
## List Comprehensions
1. Allows you to create list from other iterables.
	1. Syntax consists of square brackets [] containing expression followed by for clause, then zero or more if clauses.
Example:
```python in terminal
>>> squares = [num**2 for num in range (1, 11)] 
>>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

# Lesson 5.4
## Tuple
1. Advantages of tuples over lists:
	1. Tuples are used to store multiple items in a single variable.
	2. A tuple is a collection which is ordered and unchangeable (immutable). 
		1. Meaning we cannot change, add or remove items after the tuple has been created. 
	3. Written with round brackets.
Example:
```python
thistuple = ("apple","banana","cherry")
print(thistuple)
```
```bash
>>> ('apple','banana','cherry')
```

```python
thistuple = ("apple","banana","cherry")
print(thistuple)
```
```bash
>>> <class 'tuple'>
```

## Tuple Syntax
1. Advantages of tuples over lists:
	1. Are better suited for use with different (heterogeneous) data types.
	2. Can be used as key for dictionary.
	3. Iterating over tuples is faster.
	4. Are better for passing around data that you don’t want changed.
2. Consists of individual values separated by commas.
3. Create using parentheses.
Syntax
```python
>>> one = 'thing'
>>> one
('thing',)
>>> type(one)
<class 'tuple'>
```

# Lesson 5.5.1
## Indexing
1. Can use index operator, [], to access element in tuple. 
2. Indices start at zero.
```python
thistuple = ("apple","banana","cherry")
print(thistuple[1])
```
```bash
>>> banana
```

# Lesson 5.5.2
## Slicing
1. Allows you to access subset of tuple.
2. General syntax:
```tupleToSlice [Start index (included):Stop index (excluded):Increment]```
	1. Start index: 
		1. Index at which to start slicing. If excluded, zero is default.
		2. This element is included in slice. 
	2. Stop index:
		1. Index at which to stop slicing.
		2. This element is excluded in slice.
	3. Increment:
	4. Determines steps to take. If excluded, one is default.
Example:
```python
thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[2:5])
>>> ('cherry','orange','kiwi')
#This will return the items from position 2-5
#first item = 0
#postion 5 not included
```

# Lesson 5.6
## Tuple Methods

1. any(tuple) 
	1. Used to discover whether any element is iterable. 
	2. Returns Boolean.
2. count(item)
	1. Returns number of occurrences of item in tuple. 
3. min(tuple)
	1. Returns smallest element.
Ex.
```python
thistuple = (5,1,3,5,7,8,7,5,4,6,8,5)
x = thistuple.count(5)
print(x)
>>>4
```
4. max(tuple) 
	1. Returns largest element.
5. len(tuple)
	1. Returns total number of elements.
6. + 
	1. Used for concatenation; used in same way as lists
Ex. 
```python
thistuple = tuple(("apple","banana","cherry"))
print(len(thistuple))

>>> 3
```
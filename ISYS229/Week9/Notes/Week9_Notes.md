# Module 6 
## Dictionaries and Sets

1. Dictionaries: Data structures that hold data or information in key-value order. 
	2. Known as associative arrays in other languages. 
	3. Indexed using key which are usually strings.
	4. Two kinds:
		1. dict: Default, unordered.
		2. OrderedDict: Stores in order of insertion.
2. Set : Collection of unordered and unique data items.
	1. Able to use for mathematical operations, such as union and intersection.
		1. Union: 
			1. Given two sets, A and B, union is set of everything in A and B.
		2. Intersection: 
			1. Given two sets A and B, intersection is set of everything common in both A and B.
# Lesson 6.1
## Working with Dictionaries
1. Can create two ways:
	1. With curly brackets: dictionary = {}
	2. With dict() function: dictionary = dict()
2. Example1 shows example of how to create a dictionary.
	1. state and city are the keys.
	2. NY and New York are the values.
```python
d = dict(
	state="NY"
	city="New York"
)
```

# Lesson 6.1.1: 
## Adding Data to a Dictionary

1. Example2 shows how to add data using both curly brackets and dict() function.
	1. With dict() function, values are assigned to keys using = 
	2. With brackets, separate keys from values using colon.
```python
dict_masher = {
	"name":"Amos",
	"age":100
}
print(dict_masher)
{'name':'Amos','age':100}
```

# Lesson 6.1.3:
## Iterating through Dictionaries

1. Simplest way is to use for loop.
	1. Example: for item in dictionary
	2. By default, iterates through keys.
	3. Can specify returning keys or values using keys() or values() methods.
		1. Example, to return values: for item in dictionary.values()
	4. Use items() method to iterate through both keys and values.

# Lesson 6.1.4:
## Checking for the Existence of Particular Keys
```python
a = {
	"size":"10 feet"
	"weight":"16 pounds"
}
print("size" in a)
print("length" in a)
```

# Lesson 6.2.1:
## dict.update()

1. Inserts new key-value pairs or updates existing.
2. Syntax: dictionary.update({"key_name": "Value1"})

# Lesson 6.4: 
## The basics of Creating Sets
1.  Set is collection of data items that are unordered, unchangeable, and unique
	1. But you can remove and add items
2. Create two ways:
	1. set() function
		1. Example: a = set([1,2,3])
	2. Curly bracket notation
		1. Example: c = {'a', 'b', 'c'}

```python
thisset = {"apple","bannna","cherry"}
print(thisset)
output = {'cherry', 'apple', 'banana'}
```

# Lesson 6.4.2: 
## Adding Data to a Set
1. set.add()
	1. Adds data to set.
	2. Example: set_a.add(4)
	3. If adding duplicate value, set will not change.
2. set.update()
	1. Adds data to set using iterables.
	2. Example: set_a.update([3,4,5,6])

```python
thisset = {"apple","bannna","cherry"}
thisset.add("orange")
print(thisset)
output = {'cherry','orange', 'apple', 'banana'}
```

# Lesson 6.4.4: 
## Removing Data from a Set

1. set.pop()
2. set.remove(value)
	1. Removes passed value without returning it.
	2. If value doesn’t exist, KeyError raised.
3. set.discard(value)
	1. Removes passed value without returning it.
	2. If value doesn’t exist, no error raised.
4. set.clear()
	1. Removes all data from set

```python
thisset = {"apple","bannna","cherry"}
thisset.remove("banana")
print(thisset)
output = {'cherry', 'apple'}
```

# Lesson 6.5.1:
## Union

1. Union of two sets is set of all elements in both sets.
	1. Will always exclude any duplicates
	2. Use union() method.
		1. set_a.union(set_b) count(item)
	3. Use | operator.
		1. set_a | set_b 
```python
seta = {"a","b","c"}
setb = {1,2,3}

setc = setb | seta
{1,2,3,"b","c","a"}
```

# Lesson 6.5.2:
## Intersection

1. Intersection of sets is set of all elements that appear in all sets.
	1. Use intersection() method.
		1. set_a.intersection(set_b) count(item)
	2. Use & operator.
		1. set_a & set_b
```python
set_a={"apple","banana","cherry"}
set_b={"google","microsoft","apple"}
set_c=set_a & set_b

print(set_c)

{"apple"}
```

# Lesson 6.6:
## Frozen Sets

1. Just like sets only immutable.
2. To create, use frozenset() function.
	1. Example: a = frozenset([1,2,3])
```python
mylist = ['apple','banana','cherry']
x = (mylist)
x[1] = "strawberry"
print (x)
['apple','strawberry','cherry']

```
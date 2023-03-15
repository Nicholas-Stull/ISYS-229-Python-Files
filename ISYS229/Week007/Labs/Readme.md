# Week 7 Labs
## Creating and calling funtions
1. [3_3.py](3_4.py)

```python
# Write your code here
def skip_integers(*values):
    for x in values:
        if type(x) == int:
            continue
        print(x)
# Test you code here
skip_integers(3, 5.2, "value", 6.0)
```

2. [3_4.py](3_4.py)
```python
# Write your code here

exponential = lambda number,power : number**power

# Use the code below to test your function

print(exponential(2, 6))
```
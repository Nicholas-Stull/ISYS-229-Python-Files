# Write your code here
def skip_integers(*values):
    for x in values:
        if type(x) == int:
            continue
        print(x)

# Test you code here
skip_integers(3, 5.2, "value", 6.0)

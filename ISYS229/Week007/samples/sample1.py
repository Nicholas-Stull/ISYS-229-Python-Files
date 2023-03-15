def first_function(*values):
    for x in values:
        if type(x) == bool:
            break
        print(x)

first_function(0, "isys", "True", 3.14, "229", False, 2)
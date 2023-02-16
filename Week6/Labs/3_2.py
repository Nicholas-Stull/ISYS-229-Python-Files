answer = input("Return TRUE or FALSE: Python3 was released in 2008:\n")
answer = str(answer.upper()) #parses string value to all upper case to prepare for comparison

if answer == "TRUE": #compares variable year to YES and prints correct if a match
    print('Correct')
    print('Have a great day!')
elif answer == "FALSE": #compares variable year to NO and prints incorrect if not a match
    print('Incorrect')
    print('Have a great day!')
elif answer != ("TRUE" or "FALSE"): #determines if any other values are entered and reqeusts correct statements
    print('Please answer TRUE or FALSE')
    print('Have a great day!')


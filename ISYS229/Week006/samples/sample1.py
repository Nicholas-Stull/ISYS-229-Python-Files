#request input of true of falst from user
answer = input("Return YES or NO: Is SMC's mascot is a Roadrunner?:\n")
answer = str(answer.upper()) #parses string value to all upper case to prepare for comparison

if answer == "YES": #compares variable year to YES and prints correct if a match
    print('Correct')
elif answer == "NO": #compares variable year to NO and prints incorrect if not a match
    print('Incorrect')
elif answer != ("YES" or "NO"): #determines if any other values are entered and reqeusts correct statements
    print('Please answer YES or NO')
print("Let's Go SMC!") #Displays Let's go SMC

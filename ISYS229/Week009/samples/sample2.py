def words(parm1): #defining a function called words
    counting = {} #declaring a dictionary called counting
    
    for letters in parm1: #declaring a for loop to go through the arguments
        if letters is not ' ':
            if letters in counting:
                counting[letters] += 1
            else:
                counting[letters] = 1        
    return counting

print(words("boOkKeepEr")) #calling the words function and passing an argument, notice the difference between upper-case and lower-case
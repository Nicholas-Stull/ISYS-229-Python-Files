# Write your code here
def word_counter(string):
    # initialize an empty dictionary to store the character counts
    char_count = {}
    
    # iterate through each character in the string
    for char in string:
        # check if the character is a whitespace character
        if char.isspace():
            continue
        
        # check if the character is already in the dictionary
        if char in char_count:
            # if it is, increment the count by 1
            char_count[char] += 1
        else:
            # if it's not, add it to the dictionary with a count of 1
            char_count[char] = 1
    
    # return the dictionary of character counts
    return char_count


print(word_counter("Mississippi"))

# Write your code here
def convert_to_uppercase(word, count):
    # Check if the count is greater than the length of the word
    if count > len(word):
        count = len(word)
    
    # Convert the last 'count' letters of the word to uppercase
    result = word[:-count].lower() + word[-count:].upper()
    return result

# Take input from the user
word = input("Enter a word: ")
count = int(input("Enter the count: "))

# Call the function and print the result
print(convert_to_uppercase(word, count))

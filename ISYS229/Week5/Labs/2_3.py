import sys #import sys module
numbers = [34, 9, 32, 91, 58, 13, 77, 21, 56] #create a list of numbers
print("Array:", numbers) #print the list of numbers

# Get the user input for the number of elements to fetch from the array
count = int(input("Enter the count: "))

# Print the slice of the array from the first element to the nth element
print("Elements:", numbers[:count])


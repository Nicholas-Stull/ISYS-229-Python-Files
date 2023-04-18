# Week 8

## Assigment 
1. You will create a program which will take in a student’s name, their total quiz scores and calculate the average.
2. Based on their average quiz score, will indicate whether or not they will pass their course.
 
### Starting code:
```python
#calculating average grades using lists, by virtue of appending, sorting and using functions
name = input("Enter your first name: ") 
#takes user input for name
n = int(input("How many quizzes have you taken? " )) #takes user input for amount of total quizzes
list1 = [] #creates empty list
minimum_quizzes = 2 #declares global variable for minimum amount of quizzes needed
passing_score = 70 #declares global variable for a passing score
```
### To do list:
    1.	Create a function that will calculate the average of all quiz scores and return the value. The average should be rounded to two decimal places
    2.	Develop a conditional statement using nested if’s.If the amount of quizzes taken is greater than the minimum required quizzes then perform the following.
        1.	Develop a for loop based on the list, which takes input from the user to gather their quiz scores. I would recommend using a float data type for this input.
        2.	Make sure to append their scores into the empty list
        3.	Display their capitalized name on the screen along with their quiz scores in descending order. For example, the output should read as…
            1.	“Hello Eric, your list of quiz grades from highest to lowest are as follows: [97.30, 95.0, 93.65]”
        4.	Call the function to calculate the average scores
        5.	If the average score is greater than or equal to the passing score then do the following
            1.	Display that the user’s average, compare it against the passing score and let them know that they will pass the course
                1.	For example: The passing average is 70.00%, your average is 95.00%. Congratulations, you will pass the class.
        6.	If the average score is less than the passing score, then do the following
            1.	Display the user’s average, compare it against the passing score and let them know that they will not pass the course.
                1.	For example: The passing average is 70.00%, your average is 69.99%, YOU SHALL NOT PASS!
    3.	Otherwise, if the amount of quizzes taken is less than the minimum required quizzes, then perform the following.
        1.	Display on the screen that they must input more than the minimum quiz amount to produce a proper average.
 

### Code
```python
# Function to calculate average of quiz scores
def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return round(average, 2)


# Ask for user's first name
name = input("Enter your first name: ")

# Ask for number of quizzes taken
n = int(input("How many quizzes have you taken? "))

# Create an empty list to store quiz scores
list1 = []

# Declare minimum number of quizzes required to calculate average
minimum_quizzes = 2

# Declare passing score for the course
passing_score = 70

# Check if the user has taken enough quizzes to calculate average
if n >= minimum_quizzes:
    # Loop through the range of n quizzes and ask for user input of quiz scores
    for i in range(n):
        score = float(input("Enter quiz score: "))
        list1.append(score)

    # Sort the list of quiz scores in descending order
    list1.sort(reverse=True)

    # Display user's name and sorted list of quiz scores
    print(f"Hello {name.capitalize()}, your list of quiz grades from highest to lowest are as follows: {list1}")

    # Calculate the average of quiz scores using the defined function
    average_score = calculate_average(list1)

    # Check if the user's average score is passing or failing
    if average_score >= passing_score:
        # Display passing message
        print(
            f"The passing average is {passing_score:.2f}%, your average is {average_score:.2f}%. Congratulations, you will pass the class.")
    else:
        # Display failing message
        print(
            f"The passing average is {passing_score:.2f}%, your average is {average_score:.2f}%, YOU SHALL NOT PASS!")
else:
    # Display message that user needs to take more quizzes to calculate average
    print(
        f"You must take at least {minimum_quizzes} quizzes to produce a proper average.")
```
### Pseudocode
```pseudocode
Prompt user for their first name
Prompt user for number of quizzes taken
Create an empty list to store quiz scores
Set minimum quizzes required to calculate average to 2
Set passing score for the course to 70

If number of quizzes taken is greater than or equal to minimum quizzes required:
    Loop through the range of number of quizzes taken:
        Prompt user for quiz score
        Append quiz score to list of quiz scores
    Sort the list of quiz scores in descending order
    Display user's name and sorted list of quiz scores
    Calculate the average of quiz scores using a function
    If average score is greater than or equal to passing score:
        Display passing message
    Else:
        Display failing message
Else:
    Display message that user needs to take more quizzes to calculate average

```

### Flowchart
```mermaid
graph TD;
    A[Start] --> B[Ask for user's first name]
    B --> C[Ask for number of quizzes taken]
    C --> D[Create an empty list to store quiz scores]
    D --> E[Set minimum quizzes required to calculate average to 2]
    E --> F[Set passing score for the course to 70]
    C -- If n >= minimum quizzes --> G{Loop through the range of number of quizzes taken}
    G --> H[Prompt user for quiz score]
    H --> I[Append quiz score to list of quiz scores]
    G -- Loop back --> G
    I -- After loop --> J[Sort the list of quiz scores in descending order]
    J --> K[Display user's name and sorted list of quiz scores]
   ```
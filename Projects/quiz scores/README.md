# Week 9

## Assigment 

1. You will modify the program that you developed from last week. This time you will create an empty dictionary and update it with key value pairs of information from the user.  

### To do list:
2. Take your completed python file from last week and modify it for the following…

	1.     Change the declared empty list to an empty dictionary. If you feel it necessary, modify the name of the variable “list1” in all relevant locations throughout your code to something more appropriate.

	2.     You will need to add an input entry for the quiz name. The user will need to input the name of their individual quizzes as well as their scores. This will serve as the key value pair needed to update the dictionary variables.

	3.     Remove the defined function and calculate the rounded average using one line of code

The end result should look similar to the following…
```bash
>>> Enter your first name: eric
>>> How many quizzes have you taken? 5
>>> Enter the title of quiz number 5: Module 5
>>> Enter the score quiz 5: 89
>>> Enter the title of quiz number 4: Module 4
>>> Enter the score quiz 4: 95
>>> Enter the title of quiz number 3: Module 3
>>> Enter the score quiz 3: 92
>>> Enter the title of quiz number 2: Module 2
>>> Enter the score quiz 2: 75
>>> Enter the title of quiz number 1: Module 1
>>> Enter the score quiz 1: 80
>>> Hello Eric, the following is your quiz information:
>>> For quiz Module 5 you received 89.0%
>>> For quiz Module 4 you received 95.0%
>>> For quiz Module 3 you received 92.0%
>>> For quiz Module 2 you received 75.0%
>>> For quiz Module 1 you received 80.0%
>>> Your average quiz scores is 86.2%, which is well above the minimum 70%. Congratulations you pass the course!
```

### Code
```python
# Ask for user's first name
name = input("Enter your first name: ")

# Ask for number of quizzes taken
n = int(input("How many quizzes have you taken? "))

# Create an empty dictionary to store quiz scores
quiz_scores = {}

# Declare minimum number of quizzes required to calculate average
minimum_quizzes = 2

# Declare passing score for the course
passing_score = 70

# Check if the user has taken enough quizzes to calculate average
if n >= minimum_quizzes:
    # Loop through the range of n quizzes and ask for user input of quiz scores
    for i in range(n):
        quiz_name = input(f"Enter the title of quiz number {n-i}: ")
        score = float(input(f"Enter the score quiz {n-i}: "))
        quiz_scores[quiz_name] = score

    # Sort the list of quiz scores based on the quiz name
    sorted_scores = sorted(quiz_scores.items())

    # Display user's name and sorted list of quiz scores
    print(f"Hello {name.capitalize()}, the following is your quiz information:")
    for quiz_name, score in sorted_scores:
        print(f"For quiz {quiz_name} you received {score:.1f}%")

    # Calculate the average of quiz scores using the built-in functions
    average_score = sum(quiz_scores.values()) / len(quiz_scores)

    # Check if the user's average score is passing or failing
    if average_score >= passing_score:
        # Display passing message
        print(
            f"Your average quiz scores is {average_score:.1f}%, which is well above the minimum {passing_score}%. Congratulations you pass the course!")
    else:
        # Display failing message
        print(
            f"Your average quiz scores is {average_score:.1f}%, which is below the minimum {passing_score}%. You shall not pass!")
else:
    # Display message that user needs to take more quizzes to calculate average
    print(
        f"You must take at least {minimum_quizzes} quizzes to produce a proper average.")

```
### Pseudocode
```pseudocode
1. Ask the user for their first name and store it in a variable
2. Ask the user for the number of quizzes they have taken and store it in a variable
3. Create an empty dictionary to store quiz scores
4. Set a minimum number of quizzes required to calculate an average score
5. Set a passing score for the course
6. Loop through the range of n quizzes
    a. Ask the user for the quiz title and score
    b. Add the quiz title and score to the dictionary
7. Sort the dictionary by quiz score in descending order
8. Display the user's name and their list of quiz grades
9. Calculate the average of quiz scores using one line of code
10. Check if the user's average score is passing or failing
    a. Display passing message if the score is above the passing score
    b. Display failing message if the score is below the passing score
11. End the program
```

### Flowchart
```mermaid
graph TD;
    A[Start] --> B[Ask for user's first name]
	B --> C[Ask for number of quizzes taken]
	C --> D[Create an empty dictionary to store quiz scores]
	D --> E[Set minimum number of quizzes required to calculate average score]
	E --> F[Set passing score for the course]
	F --> G[Loop through range of n quizzes]
	G --> H[Ask for quiz title and score]
	H --> I[Add quiz title and score to dictionary]
	I --> G
	G --> J[Sort dictionary by quiz score in descending order]
	J --> K[Display user's name and list of quiz grades]
	K --> L[Calculate average of quiz scores using one line of code]
	L --> M[Check if user's average score is passing or failing]
	M -- Yes --> N[Display passing message]
	M -- No --> O[Display failing message]
	N --> P[End program]
	O --> P
   ```
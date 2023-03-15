# Week 10

## Assigment 
This week, you will have the option the develop two separate programs. You may choose option A or option B.
### To do list:
### Option A: 
1.	Create a program that performs the following…
    1.	Create input statements that will take in a student’s first name, last name, major, and the amount of school credits they’ve taken so far.
    2.	Declare a Student class. Within the class develop the following attributes
        1.	Define an init method with the following attributes:
            1.	First name, last name, major, and credits
        2.	Define a method that will take the amount of school credits taken and determine if the student is eligible to schedule their It internship.	
    3.	Instantiate a new object using the Student class by passing the inputs that the user typed in.
    4.	Display the user’s first and last name capitalized. Show them the major and the amount of credits they just typed in.
    5.	Call the instantiated object using the method to determine if they are eligible to schedule their internship
2.	Make sure to provide a flowchart and pseudocode for this program. Along with the program file Module7_lastname.py.
3.	The end result should look similar to the following…  
![[Picture1.jpg]]
### Option B: 
1. Create a program that performs the following using the tkinter import module…
	1. Create a self-window
	2. Add labels and entries for personal information
	3. Add a button to check eligibility for an internship
	4. Add a label to display the result
	5. Add the main event loop
2.	If you decide to perform option B, you do not have to perform a flowchart pseudocode. You will only be responsible for uploading a completed .py file. Make sure to label it Module7_lastname.py 
3.	The output should look similar to this
![[Picture2.jpg]]
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
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

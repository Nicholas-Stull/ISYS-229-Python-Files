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

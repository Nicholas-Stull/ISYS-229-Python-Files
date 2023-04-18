# Get the user's first and last name
first_name = input("What is your first name? ").capitalize()
last_name = input("What is your last name? ").capitalize()

# Get the days the user has class
days = input(
    "What days do you have class? (Please enter as comma-separated list) ").split(",")
days = [day.strip().capitalize() for day in days]

# Get the days of the week
weekdays = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

# Calculate the days the user doesn't have class
no_class = [day for day in weekdays if day not in days]

# Output the results
print(
    f"Thank you, {first_name} {last_name}, you have class on these days: {', '.join(days)}.")
print(f"You don't have class on these days: {', '.join(no_class)}.")

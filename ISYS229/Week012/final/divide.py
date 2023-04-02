# Import the get_random_quote function from the random_quote_generator module
import tkinter as tk
# Define a function for dividing two numbers entered in the GUI
from random_quote_generator import get_random_quote


def divide_numbers():  
# Get the numbers entered in the GUI and convert them to floats
    try:  
        # Divide the numbers and set the text of the result label to the result
        num1 = float(num1_entry.get())
        # Divide the numbers and set the text of the result label to the result
        num2 = float(num2_entry.get())
        result = num1/num2  # Divide the numbers and set the text of the result label to the result
        # Divide the numbers and set the text of the result label to the result
        result_label.config(text=f"Result: {result}")
    except ValueError:  # If the numbers entered are not valid, display an error message
        # Divide the numbers and set the text of the result label to the result
        result_label.config(text="Please enter valid numbers")
    except ZeroDivisionError:  # If the second number is zero, display an error message
        # Divide the numbers and set the text of the result label to the result
        result_label.config(text="Cannot divide by zero")
    finally:  # Clear the entry fields after the function is run
        # Divide the numbers and set the text of the result label to the result
        num1_entry.delete(0, tk.END)
        # Divide the numbers and set the text of the result label to the result
        num2_entry.delete(0, tk.END)


def generate_quote():  # Get a random quote and set the text of the quote label to the quote
    # Get a random quote and set the text of the quote label to the quote
    quote_text = get_random_quote(wordcount=20)
    # Get a random quote and set the text of the quote label to the quote
    quote_label.config(text=quote_text)


root = tk.Tk()  
# Create the root window for the GUI
root.title("Divide them numbers!")  
# Set the title of the GUI
num1_label = tk.Label(root, text="Enter first number:")
# Create a label and an entry field for entering the first number in the GUI
num1_label.grid(row=1, column=0)
# Place the label and entry field in the GUI
num1_entry = tk.Entry(root)
# Create a label and an entry field for entering the first number in the GUI
num1_entry.grid(row=1, column=1)
# Place the label and entry field in the GUI

num2_label = tk.Label(root, text="Enter second number:")
# Create a label and an entry field for entering the second number in the GUI
num2_label.grid(row=2, column=0)
# Place the label and entry field in the GUI
num2_entry = tk.Entry(root)
# Create a label and an entry field for entering the second number in the GUI
num2_entry.grid(row=2, column=1)
# Place the label and entry field in the GUI

divide_button = tk.Button(root, text="Divide", command=divide_numbers)
# Create a button to run the divide_numbers function
divide_button.grid(row=3, column=0)
# Place the button in the GUI

result_label = tk.Label(root, text="", anchor="center", justify="center")
# Create a label to display the result of the division
result_label.grid(row=5, column=0, columnspan=2, sticky="nsew")
# Place the label in the GUI

quote_button = tk.Button(root, text="Generate Quote", command=generate_quote)
# Create a button to run the generate_quote function
quote_button.grid(row=3, column=1)
# Place the button in the GUI

quote_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=250)
# Create a label to display the quote
quote_label.grid(row=7, column=0, columnspan=2, sticky="nsew", pady=(10, 0))
# Place the label in the GUI
root.geometry("270x280")
# Set the size of the GUI
root.mainloop()
# Run the GUI
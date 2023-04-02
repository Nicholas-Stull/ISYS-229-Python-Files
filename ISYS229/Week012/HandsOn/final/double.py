# Import the tkinter module for creating the GUI
import tkinter as tk
# Import the get_random_quote function from the random_quote_generator module
from random_quote_generator import get_random_quote


# Define a function for doubling a number entered in the GUI
def double_number():
    try:
        # Get the number entered in the GUI and convert it to an integer
        num = int(num_entry.get())
        result = num*2  # Double the number
        # Set the text of the result label to the doubled number
        result_label.config(text=f"Result: {result}")
    except ValueError:
        # If the number entered is not a valid integer, display an error message
        result_label.config(text="Please enter a valid integer")
    finally:
        # Clear the entry field after the function is run
        num_entry.delete(0, tk.END)


# Define a function for generating a random quote in the GUI
def generate_quote():
    # Call the get_random_quote function to generate a quote
    quote_text = get_random_quote(wordcount=20)
    # Set the text of the quote label to the generated quote
    quote_label.config(text=quote_text)


# Create the root window for the GUI
root = tk.Tk()
root.title("Double that number!")  # Set the title of the GUI


# Create a label and an entry field for entering a number in the GUI
num_label = tk.Label(root, text="Enter first number:")
num_label.grid(row=1, column=0)
num_entry = tk.Entry(root)
num_entry.grid(row=1, column=1)


# Create a button for doubling the number entered in the GUI
double_button = tk.Button(root, text="Double #", command=double_number)
double_button.grid(row=3, column=0)


# Create a label for displaying the result of doubling the number entered in the GUI
result_label = tk.Label(root, text="", anchor="center", justify="center")
result_label.grid(row=5, column=0, columnspan=2, sticky="nsew")


# Create a button for generating a random quote in the GUI
quote_button = tk.Button(root, text="Generate Quote", command=generate_quote)
quote_button.grid(row=3, column=1)


# Create a label for displaying the generated quote in the GUI
quote_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=250)
quote_label.grid(row=7, column=0, columnspan=2, sticky="nsew", pady=(10, 0))


# Set the size of the GUI window
root.geometry("270x280")


# Start the GUI main loop
root.mainloop()

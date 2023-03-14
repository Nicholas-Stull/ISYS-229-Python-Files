import tkinter as tk
import tkinter.ttk as ttk
import sv_ttk

class InternshipChecker:
    def __init__(self, master):
        self.master = master
        master.title("Internship Checker")
        master.geometry("400x400")

        # Labels and Entries for personal information
        self.first_name_label = ttk.Label(master, text="First Name:")
        self.first_name_label.pack()
        self.first_name_entry = ttk.Entry(master)
        self.first_name_entry.pack()

        self.last_name_label = ttk.Label(master, text="Last Name:")
        self.last_name_label.pack()
        self.last_name_entry = ttk.Entry(master)
        self.last_name_entry.pack()

        self.major_label = ttk.Label(master, text="Major:")
        self.major_label.pack()
        self.major_entry = ttk.Entry(master)
        self.major_entry.pack()

        self.credits_label = ttk.Label(master, text="Credits:")
        self.credits_label.pack()
        self.credits_entry = ttk.Entry(master)
        self.credits_entry.pack()

        # Button to check eligibility for an internship
        self.check_button = ttk.Button(
            master, text="Check Eligibility", command=self.check_eligibility)
        self.check_button.pack()

        # Label to display the result
        self.result_label = ttk.Label()
        self.result_label.pack()

    def check_eligibility(self):
        try:
            # Retrieve values from entries
            first_name = self.first_name_entry.get()
            last_name = self.last_name_entry.get()
            major = self.major_entry.get()
            credits = int(self.credits_entry.get())

            # Check eligibility based on criteria
            if credits >= 125 and major.lower() == "it":
                message = f"Congratulations {first_name} {last_name}, you are eligible for an internship!\nThe Minimum credits for the internship is 125"
            else:
                message = f"Sorry {first_name} {last_name}, you are not eligible for an internship.\nThe Minimum credits for the internship is 125"

            # Display result
            self.result_label.config(text=message)

        except ValueError:
            # Handle ValueError if credits is not an integer
            self.result_label.config(text="Credits must be an integer.")


# Create Tk instance
root = tk.Tk()

# Set the theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

# Instantiate InternshipChecker object
app = InternshipChecker(root)

# Start main event loop
root.mainloop()

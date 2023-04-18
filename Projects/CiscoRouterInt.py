from tkinter import *
from netmiko import ConnectHandler

# Function to execute the "List running Cisco configurations" command and display the output


def execute_command(): # Get the command specified by the user
    # Get the command specified by the user
    command = command_entry.get()

    # Authenticate to the router using netmiko
    router = {
        'device_type': 'cisco_ios',
        'ip': ip_entry.get(),
        'username': username_entry.get(),
        'password': password_entry.get()
    }
    net_connect = ConnectHandler(**router)
    net_connect.enable()

    # Execute the specified command and get the output
    output = net_connect.send_command(command)

    # Display the output in the text box
    output_text.delete(1.0, END)
    output_text.insert(END, output)

    # Disconnect from the router
    net_connect.disconnect()
def list_configurations(): # Used for running the "show running-config" command
    # Authenticate to the router using netmiko
    router = {
        'device_type': 'cisco_ios',
        'ip': ip_entry.get(),
        'username': username_entry.get(),
        'password': password_entry.get()
    }
    net_connect = ConnectHandler(**router)
    net_connect.enable()

    # Execute the "show running-config" command and get the output
    output = net_connect.send_command("show running-config")

    # Display the output in the text box
    output_text.delete(1.0, END)
    output_text.insert(END, output)

    # Disconnect from the router
    net_connect.disconnect()

# Function to execute the "Show the iOS version" command and display the output


def show_ios_version(): # Used for running the "show version" command
    # Authenticate to the router using netmiko
    router = {
        'device_type': 'cisco_ios',
        'ip': ip_entry.get(),
        'username': username_entry.get(),
        'password': password_entry.get()
    }
    net_connect = ConnectHandler(**router)
    net_connect.enable()

    # Execute the "show version" command and get the output
    output = net_connect.send_command("show version")

    # Display the output in the text box
    output_text.delete(1.0, END)
    output_text.insert(END, output)

    # Disconnect from the router
    net_connect.disconnect()

# Function to execute the "Identify the local IP information on the router" command and display the output


def identify_local_ip(): # Used for running the "show ip interface brief" command
    # Authenticate to the router using netmiko
    router = {
        'device_type': 'cisco_ios',
        'ip': ip_entry.get(),
        'username': username_entry.get(),
        'password': password_entry.get()
    }
    net_connect = ConnectHandler(**router)
    net_connect.enable()

    # Execute the "show ip interface brief" command and get the output
    output = net_connect.send_command("show ip interface brief")

    # Display the output in the text box
    output_text.delete(1.0, END)
    output_text.insert(END, output)

    # Disconnect from the router
    net_connect.disconnect()


def clear_output():
    output_text.delete(1.0, END)




# Create a Tkinter window
root = Tk()
root.title('Cisco Router Command Execution')


# Add labels and entry boxes for user input
Label(root, text="Router IP Address").grid(row=0)
ip_entry = Entry(root)
ip_entry.grid(row=0, column=1)

Label(root, text="Username").grid(row=1)
username_entry = Entry(root)
username_entry.grid(row=1, column=1)

Label(root, text="Password").grid(row=2)
password_entry = Entry(root, show="*")
password_entry.grid(row=2, column=1)

Label(root, text="Command").grid(row=3)
command_entry = Entry(root)
command_entry.grid(row=3, column=1)

# Add a button to execute the command
Button(root, text="Execute Command",
       command=execute_command).grid(row=3, column=2)

Label(root, text="Commands").grid(row=0, column=3)
# Add buttons to execute each command
Button(root, text="List running Cisco configurations",
       command=list_configurations).grid(row=1, column=3)
Button(root, text="Show the iOS version",
       command=show_ios_version).grid(row=2, column=3)
Button(root, text="Identify the local IP information on the router",
       command=identify_local_ip).grid(row=3, column=3)
# Add a button to clear the output
Button(root, text="Clear output", command=clear_output).grid(row=4, column=1)
# Add a button to exit the program
Button(root, text="Exit", command=root.quit).grid(row=4, column=2)


# Add a text box to display the output
Label(root, text="Output").grid(row=4, column=0)
output_text = Text(root, height=10, width=50)
output_text.grid(row=5, columnspan=3)

# Start the Tkinter event loop
root.mainloop()

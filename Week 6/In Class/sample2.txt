#Ask user for user name
user_name = input("Enter your User Name: ")

#This is a stored clear text password
stored_password = "Pa$$w0rd"

#control variable initiated to value of False
require_auth = True

#Loop while authentication is set to false
while require_auth == True:
    password = input("Enter your password: ") #asks for user password
    if password == stored_password: #compares user input to stored password
        print(f"Welcome back {user_name} ") #displays user name with Welcome Back
        require_auth = False #sets authentication to True in order to exit While loop
    else:
        print("Incorrect password, try again... ") #asks user to try again and remains in while loop

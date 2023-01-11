from time import sleep


userName = input("What is your name? ")
userAge = input("How old are you? ")
dont = "Don't drink and drive"
drive = "Drive sober"
print("Hello " + userName)
   
if int(userAge) >= 21:
    print("Lets go drink!")
elif 18 <= int(userAge) <= 21: 
    print("Can't drink today, try in Canada")
else:
    print("you can't drink")
#sleep(1)


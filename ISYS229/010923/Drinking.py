from time import sleep


userName = input("What is your name? ")
userAge = input("How old are you? ")

print("Hello " + userName)
   
if int(userAge) >= 21:
    print("Lets go drink!")
elif 18 <= int(userAge) <= 21: 
    print("Can't Drink today, head Go to Canada")
else:
    print("Not Today")
sleep(1)
print("Don't Drink and Drive")
print("Drive Sober")
#if 10000 <= number <= 30000:
#elif int(userAge) 18 >= 21:
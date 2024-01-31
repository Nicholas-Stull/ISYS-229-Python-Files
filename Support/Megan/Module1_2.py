import sys
from icecream import ic

# name and age inputs
name_first = input("Your first name: ")
name_last = input("Your middle name: ")
Age_number = input("Your age: ")
# number varible inputs
Weight_p = int(input("Your weight in lbs: "))
height_f = int(input("Your height in feet: "))
# conversions
weight_k = Weight_p * 0.045 
ic(weight_k)
weight_o = Weight_p * 16
height_m = height_f * 0.3048

# the results statments
# print ("Hello", name_first, name_last,".", "Your weight in Kilometers is", weight_k, "and your weight in ounces is", weight_o, ". Your height in meters is", height_m, ".")

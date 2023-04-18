
#set variable for minimum_meal = 20
minimum_meal = 20

# define a function called StateTax to calculate 6% sales tax and return
def StateTax(price):
    """Calculate 6% sales tax on the given price and return it"""
    return 0.06 * price

# define a function called tip_calc to calculate the return tip
def tip_calc(grand_total): 
    # if the price of the meal is greater than or equal the minimum meal amount
    # then the rate of the tip will be 20% otherwise it will be 15%
    """Calculate the return tip based on the price of the meal and the minimum meal amount"""
    if grand_total >= minimum_meal:
       gratuity = (0.2 * grand_total)
    else:
        gratuity = (0.15 * grand_total)
    return(gratuity)



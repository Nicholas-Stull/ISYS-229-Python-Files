from tax_and_tip import StateTax, tip_calc
# from “module” import “appropriate functions”


def main():  # defining main function call for user input
    name = str(input("Please enter customer name: ")).capitalize()
    price = float(input('Enter the price of the meal: '))
    display_results(name, price)
    
# Develop a function that will perform the following:
def display_results(name, price):
    tax = StateTax(price)
    grand_total = price + tax
    print("Customer name:", name)  # display the name of the customer
    print("Original price is:", price) # display the original price: “Original price is…”
    print("State tax is:", tax) # display the sales tax: “State tax is…”
    print("Grand total is:", grand_total)
    gratuity = tip_calc(grand_total)
    print("Recommended gratuity is:", gratuity)


main()  # calling main function





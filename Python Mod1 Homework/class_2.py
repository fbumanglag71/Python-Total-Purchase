## Author: Francisco Bumanglag
## Project: Total Purchase Program
## Assignment: Module 1 Project 2
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 18, 2023


#INPUT SCREEN 
item1 = float(input('Enter the price for item #1: '))
item2 = float(input('Enter the price for item #2: '))
item3 = float(input('Enter the price for item #3: '))
item4 = float(input('Enter the price for item #4: '))
item5 = float(input('Enter the price for item #5: '))

#CALCULATIONS
subtotal = item1 + item2 + item3 + item4 + item5
sales_tax = subtotal * .07
finalTotal = subtotal + (.07 * subtotal)

#OUTPUT 
print('Your subtotal is: ${:.2f}'.format(subtotal))
print('Your sales tax is: ${:.2f}'.format(sales_tax))
print('Your final total for your purchased items is: ${:.2f}'.format(finalTotal))








#eboyd-f18p-itc110-a3.py
#This program finds the cost per square inch of a 14-inch pizza

from math import *

def main():
    d = int(input("Enter the size of your pizza in inches: "))
    price = int(input("Enter the cost of your pizza in cents: "))
    pizza = pi * ((d/2) ** 2)
    cost = price / pizza, 2
    #costFormatted = round(cost)

    print("Your pizza costs", cost, "cents per square inch")

main()
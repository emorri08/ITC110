#eboyd-f18p-itc110-a3.py
#This program finds the cost per square inch of a 14-inch pizza

from math import *
from graphics import *

def main():
    win = GraphWin("Pizza Calculator", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    #interface
    Text(Point(1,3), "Enter the size of your pizza (in inches):").draw(win)
    Text(Point(1,1), "Enter the cost of your pizza (in cents):").draw(win)
    inputText = Entry(Point(2.25,3), 5)
    inputText2 = Entry(Point(2.25,6), 5)
    inputText.setText("0.0")
    inputText.draw(win)
    inputText2.setText("200.0")
    inputText2.draw(win)
    button = Text(Point(1.5,2.0),"Calculate Cost!")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)

    #wait for click
    win.getMouse()

    #Calcluate cost of pizza
    d = int(input("Enter the size of your pizza in inches: "))
    price = int(input("Enter the cost of your pizza in cents: "))
    pizza = pi * ((d/2) ** 2)
    cost = round(price / pizza, 2)

    #display calculation and change button to "quit" button
    outputText.setText("Your pizza costs", cost, "cents per square inch.")
    button.setText("Quit")

    #wait for click, quit program
    win.getMouse()
    win.close()

main()
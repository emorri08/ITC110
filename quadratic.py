#quadratic.py
#compute the real roots of a quadratic equation
#the program will crash if the equation has no real roots

from math import *

def main():
    print("This program finds the real solutions to a quadratic")
    print()

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discRoot = sqrt(b * b - 4 * a * c)

    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are", root1, ",", root2)

main()

#quadratic2.py
#calculate the two solutions to the quadratic equations

from math import *

def main():
    print("find the real solutions to a quadratic")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        discRoot = sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("The solutions are", root1,",", root2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("No real roots")
        else:
            print("Invalid coefficient given")
    except: #equiv of else statement in if/else
        print("something went wrong, sorry dude")

if __name__ == '__main__':
    main()

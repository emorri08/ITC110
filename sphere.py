#sphere.py
#calculate the area and volume of a sphere

from math import * #alternative would be import math

def main():
    print("This program calculates the area and volume of a sphere.")
    print()

    r = float(input("Enter the radius of the sphere: "))

    volume = 4.0 / 3 * pi * r ** 3
    area = 4.0 * pi * pow(r, 2)

    print("The volume is", volume)
    print("The area is", area)

main()

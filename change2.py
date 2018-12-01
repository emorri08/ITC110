#change2.py
#version 2

def main():
    print("Change Counter")

    print("Enter the count for each coin type: ")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1

    print("The total value of the change is ${0}.{1:0>2}"
    .format(total//100, total%100))

main()
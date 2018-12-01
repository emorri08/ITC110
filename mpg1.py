#mpg1.py
#calculate miles per gallon driven

def main():
    #greeting
    print("Calculate miles per gallon")
    print()

    #input
    miles = float(input("enter miles driven: "))
    gallons = float(input("enter gallons of gas used: "))

    if miles <= 0:
        print("miles must be greater than zero")
    elif gallons <= 0:
        print("gallons must be greater than zero")
    else:
        #calculate
        mpg = round(miles/gallons, 2)
        print("Miles per gallon:",mpg)

    print("buh bye, bitches")

main()
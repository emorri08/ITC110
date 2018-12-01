#mpg2.py
#calculate miles per gallon driven
#alternate syntax

def main():
    #greeting
    print("Calculate miles per gallon")
    print()

    anotherTrip = "y" #set to yes to get loop started. If set to n, it will skip the loop and just say goodbye
    while anotherTrip == "y":

        #input
        miles = float(input("enter miles driven: "))
        gallons = float(input("enter gallons of gas used: "))
    
        if miles > 0 and gallons > 0:
            #calculate
            mpg = round(miles/gallons, 2)
            print("Miles per gallon:", mpg)
        else:
            print("both entries must be greater than zero")

        anotherTrip = input("Get entries for another trip? (y/n) ")

    print("buh bye, bitches")

main()
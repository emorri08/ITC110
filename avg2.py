#avg2.py
#ask user for moredata

def main():
    total = 0.0
    #create a counted variable
    count = 0
    moredata = "yes"

    while moredata[0] == "y":
        x = float(input("Enter a number >>> "))
        total = total + x
        count = count + 1
        moredata = input("Do you have more numbers (yes/no)? ")
    print("The average of the numbers is", total / count)
main()
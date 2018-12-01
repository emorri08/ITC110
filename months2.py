#months2.py
# second version - improved

def main():
    # create a list of months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    n = eval(input("Enter a number 1-12: "))

    print("The month is", months[n-1]+".")

main()

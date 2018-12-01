#change.py
#calculate the value of change entered by the user
#we will avoid the eval function

def main():
    print("Change converter")
    print() #print without arguments prints blank line
    print("Enter the count for each type of coin")
    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))

    #calculate the total in dollars and cents
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies

    #display the result
    print()
    print("The total value of your change is $" +str(round(total,2)))

main()

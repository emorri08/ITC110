#grades.py
#grade calculator
#simple program that converts a numeric quiz score
#and converts it to a letter grade

def main():
    #get user input and store it in a variable
    score = int(input("Enter your quiz score: "))

    if score == 5:
        print("A")
    elif score == 4:
        print("B")
    elif score == 3:
        print("C")
    elif score == 2:
        print("D")
    elif score <= 1:
        print("FAIL")

    else:
        print("your score must be between 1 and 5")

main()
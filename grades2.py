#grades2.py
#grade calculator
#simple program that converts a numeric exam score
#to a letter grade

def main():
    #get user input and store it in a variable
    score = int(input("Enter your exam score: "))
    #conditional statement:
    if score >= 90 and score <= 100:
        print("A")
    elif score >= 80 and score <= 89:
        print("B")
    elif score >= 70 and score <= 79:
        print("C")
    elif score >= 60 and score <= 69:
        print("D")
    elif score < 60:
        print("FAIL")
    else:
        print("Your score must be between 0 and 100")

main()
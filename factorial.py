#factorial.py
#calculate the factorial of 6

def main():
    n = int(input("Enter a whole number to calculate its factorial: "))
    fact = 1
    #for factor in (range(2, n+1)):
    for factor in range(n, 1, -1):
        print(factor)
        fact = fact * factor
    print("The factorial of n is:", fact)

main()

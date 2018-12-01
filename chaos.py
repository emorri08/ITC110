#chaos.py
#a simple program illustrating chaotic behavior

def main():
    print("This is a simple program illustrating chaotic behavior.")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many times should I print?"))
    for i in range(n):
        x = 3.9 * x * (1-x)
        print(x)

main()

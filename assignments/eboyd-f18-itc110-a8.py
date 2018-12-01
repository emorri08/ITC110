#eboyd-f18-itc110-a8.py
#fibonacci sequence

def main():
    num = int(input("Enter your number: "))

    x, y = 1, 1
    for i in range(num - 2):
        x, y = x + y, x
    print("Your fibonacci number is:", x)

main()

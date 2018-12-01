#avg3.py
#use negative number as a sentinel (stops loop)

def main():
    total = 0.0
    count = 1
    x = float(input("Enter a number (negative # = quit: "))
    while  x >= 0:
        total = total + x
        count = count + 1
        x = float(input("Enter a number (negative # = quit: "))
    print("The average is", total / (count -1))
    print(count)
main()
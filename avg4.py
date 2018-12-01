#avg4.py
#use enter to quit

def main():
    total = 0.0
    count = 1
    xStr = input("Enter a number (<Enter> to quit): ")
    while xStr != "":
        x = float(xStr)
        total = total + x
        count = count + 1
        xStr = input("Enter a number (<Enter> to quit): ")

    print("The average of the number is", total/(count - 1))
main()
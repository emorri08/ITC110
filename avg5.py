#avg5.py
#read from a file

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, "r")
    total = 0
    count = 0
    for line in infile:
        total = total + float(line)
        count = count +  1
    print("The average of the numbers is", total / count)
main()
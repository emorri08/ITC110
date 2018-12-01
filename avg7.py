#avg7.py

def main():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, "r")
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        #update the  count and the total for the values in the line
        for xStr in line.split(","):
            total = total + float(xStr)
            count += 1 # shortened --> count = count + 1
        line = infile.readline()
    print("The average of the numbers is", total / count)
main()
#printfile.py
#print a file to the screen

def main():
    fname = input("Enter the filename: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)

main()
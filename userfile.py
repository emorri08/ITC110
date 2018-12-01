#userfile.py
# batch processing of a file to produce user names
# read from names.txt, write names to separate file

def main():
    print("Create a file of user names from a file of names.")

    #get the file names
    infileName = input("What file are the names in? ")
    outfileName = input("What file should the user names go in? ")

    #open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    #process each line of the input file
    for line in infile:
        #get the first and last name from the file
        first, last = line.split()
        #create username
        uname = (first[0] + last[:7]).lower()
        #write to the output file
        print(uname, file=outfile)

    #close the files
    infile.close()
    outfile.close()

    print("usernames have been written to", outfileName)

main()

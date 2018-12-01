#numbers2text.py
# convert a unicode sequence to a string

def main():
    print("convert a unicode sequence to a string")

    # get the sequence
    inString = input("Enter the unicode encoded message: ")

    #loop through each substring and build the message
    msg = ""
    for numStr in inString.split():
        codeNum = int(numStr) #converting text digits to a number
        msg = msg + chr(codeNum) #concat the char to the message

    print("The decoded message is",msg)

main()

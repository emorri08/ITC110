#eboyd-f18-itc110-a5.py
# program that gets a string from the user and
# returns the number of words in that sentence.

def main():
    print("Word Counter")
    #a little  extra space
    print("")

    #prompt the user to enter a string
    txt = input("Please enter a string of words to be counted: ")
    #split and get the length of the string
    wrdCount = len(txt.split())
    charCount = len(txt)

    #a little more space
    print(" ")
    print("You entered",wrdCount,"words.")
    print("")
    print("The",wrdCount,"words you entered contain",charCount,"characters.")
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - -")

main()

# text2numbers.py
# converyt a text message into a sequence of numbers
# from the unicode table

def main():
    print("Convert a text message into a sequence of numbers")

    #ask user for the message to encode
    msg = input("Enter the message to encode: ")

    print("Here are the unicode codes: ")

    for ch in msg:
        print(ord(ch) +(420-187), end=" ")

    print() #end line the output

main()

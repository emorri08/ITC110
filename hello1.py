#hello1.py
#version 2

def greet(person):
    print("Hello",person+", how are you?")
    print("Salsa is a cat, ",person+". Gaucho is also a cat. Abby is a cat, too.")

def main():
    #get user input
    person = input("Enter your name ")
    greet (person)

main()

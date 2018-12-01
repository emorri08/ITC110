#convert2.py
#add cold and hot weather warnings

def main():
    celsius = float(input("What is the celsius temp? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    #print the warnings
    if fahrenheit > 90:
        print("It's hot out bitch! Wear sunscreen")
    elif fahrenheit < 30:
        print("Brrrr bitch! Wear a jacket")
    else:
        print("aww bitch...its nice out")
    print("Buh bye bitch!")

main()
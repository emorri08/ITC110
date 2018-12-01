#convert.py
#convert Celsius to Fahrenheit

def main():
    for i in range(5):
        #input
        celsius = eval(input("What is the Celsius temp? "))
        #processing -- need another variable to store the result
        fahrenheit = 9/5 * celsius + 32
        #output
        print("The temp is", fahrenheit, "degrees Fahrenheit")
        input("Press the <Enter> key to quit.")

main()

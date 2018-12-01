#convert.py
#convert Celsius to Fahrenheit in 10 degree increments

def main():
    print("Celsius to Fahrenheit")
    print("---------------------")
    print(" 0            32.0")
    for celsius in [10,20,30,40,50,60,70,80,90]:
        fahrenheit = 9/5 * celsius + 32
        print(celsius,"          ",fahrenheit)
    print("100           212.0")

main()

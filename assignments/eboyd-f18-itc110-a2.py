# eboyd-f18-itc110-a2.py
# This program converts Kilometers to Miles

def main():
    for i in range(1):
        factor = 0.621371
        km = eval(input("Enter distance in Kilometers: "))
        mi = km * factor
        print("You travelled ",mi," miles.")
        
main()

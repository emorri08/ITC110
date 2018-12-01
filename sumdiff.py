#sumdiff.py
# calculate sum and difference of two numbers

#define the function
def sumDiff(x,y):
    sum = x + y
    diff = x - y
    return sum, diff

def main():
    num1, num2 = input("Enter two numbers, comma separated: ").split(",")
    #call the function
    s, d = sumDiff(float(num1),float(num2))
    print("Sum:",s,"Diff",d)

main()
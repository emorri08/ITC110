#eboyd-f18-itc110-a7.py
# payroll calculator

def main():
    print('Payroll Calculator')
    print()

    #create a variable to store the number of hours that the user worked
    hrs = float(input('Please enter the number of hours you worked this week: '))
    #create a variable to store the user's hourly pay rate
    rate = float(input('Please enter your hourly rate: '))

    if hrs > 40:
        #calculate number of hours over 40
        ot = hrs - 40
        #calculate overtime pay
        otPay = ot * rate * 1.5
        #calculate regular pay
        regPay = rate * 40
        #total pay
        totalPay = (otPay + regPay)
        print('Your weekly pay is', round(totalPay,2), 'dollars.')
    elif hrs <= 40:
        regPay = round(rate * hrs)
        #convert reg pay to a string
        str(regPay)
        print('Your weekly pay is', round(regPay,2), 'dollars.')
main()
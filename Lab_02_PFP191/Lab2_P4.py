import math
def calculate(d, i, n):
    r = math.pow(d + d*i, n)
    print('The amount received after', n, 'years:', r)
while True:
    try:
        d = int(input('Enter intitial deposit: '))
        i = float(input('Enter interest: '))
        n = int(input('Enter number of year of deposit: '))
        if d >= 1000000:
            if 0 < i < 1:
                calculate(d, i, n)
                break
            else:
                print('Interest must be < 0 and > 1')
        else:
            print('Intitial deposit amount must be >= 1000000')
    except:
        print('Invalid input')

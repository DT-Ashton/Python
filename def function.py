def print_divisor(n):
    i = 2
    x = int(n/2)
    while i <= x:
        if n%i == 0:
            print(i)
        i += 1

def sum_divisor(n):
    i = 2
    total = 0
    x = int(n/2)
    while i <= x:
        if n%i == 0:
            total += 1
        i += 1
    return total

while True:
    try:
        n = int(input('Enter n: '))
        print('Divisor of n:')
        print_divisor(n)
        print('Sum divisors:', sum_divisor(n))
        break
    except:
        print('Invalid input')

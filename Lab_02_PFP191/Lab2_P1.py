# S1 = 1 + 2 + 3 +...+ n
def sum_int(n):
    S1 = 0
    for i in range(1, n + 1):
        S1 = S1 + i
    print('S1 =', S1)

# S2 = n! = 1 * 2 * 3 *...* n
def print_factorial(n):
    S2 = 1
    for i in range(1, n + 1):
        S2 = S2 * i
    print('S2 =', S2)

# S3 = 1 + 1/2 + 1/3 +...+ 1/n
def sum_faction(n):
    S3 = 0
    for i in range(1, n + 1):
        S3 = S3 + 1/i
    print('S3 =', S3)

# Check whether n is a prime number or not
def check(n):
    if n > 1:
        for i in range(2, int(n/2) + 1):
            if n % i == 0:
                print('n is not a prime number')
                break
        else:
            print('n is a prime number')
    else:
        print('n is not a prime number')


while True:
    try:
        n = int(input('Enter integer n: '))
        if n > 5:
            sum_int(n)
            print_factorial(n)
            sum_faction(n)
            n = int(input('Re-enter n: '))
            check(n)
            break
    except:
        print('Invalid input')

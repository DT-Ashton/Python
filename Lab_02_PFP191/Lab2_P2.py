import math

# Display all common prime dividers
def display(m, n):
    for i in range(2, int(math.sqrt(min(m, n)) + 1)):
        if m % i == 0 and n % i == 0:
            if i == 2 or i == 3 or i == 5 or i == 7:
                print(i)
            elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
                print(i)

def find_gcd(m, n):
    GCD = math.gcd(m, n)
    print('GCD:', GCD)


def find_lcm(m, n):
    LCM = math.lcm(m, n)
    print('LCM:', LCM)
    
m = int(input('Enter integer m: '))
n = int(input('Enter integer n: ')) 
display(m, n)
find_gcd(m, n)
find_lcm(m,n)

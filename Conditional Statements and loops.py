
# Homework
# 1:
numbers = list()
for n in range(1500, 2701):
    if n % 7 == 0 and n % 5 == 0:
        numbers.append(n)
print(numbers)

# 2:
c = 60
f = 45
celsius = ((f - 32) * 5 // 9)
fahrenheit = (9 * c + 32 * 5) // 5
print(f'{f} degrees Fahrenheit is {celsius} degrees Celsius')
print(f'{c} degrees Celsius is {fahrenheit} degrees Fahrenheit')

# 3:
import random
number = random.randint(1, 9)
while True:
    guess = int(input('Guess a number between 1 and 9: '))
    if guess == number:
        print("Well guessed!")
        break

# 4:
for i in range(0, 5):
    for j in range(i):
        print('*', end=' ')  # end='' ensures printing in the same line
    print('')  # print nothing so it can move to the next line
for i in range(5, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print('')

# 5:
word = input('Enter a word: ')
char = [x for x in word]
char.reverse()
reversed_word = ''.join(c for c in char)
print('Reversed word: ' + reversed_word)

# 6:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print('Number of even number:', even)
print('Number of odd numbers:', odd)

# 7:
data_list = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for item in data_list:
    print(item, type(item))

# 8:
for i in range(6):
    if i == 3:
        continue
    else:
        print(i, end=' ')

# 9:
a = 0
b = 1
while True:
    print(b, end=' ')
    c = a + b
    a = b
    b = c
    if c >= 50:
        break

# 10:
for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Frizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 11:
m = 3  # row
n = 4  # column
arr = [[0 for col in range(n)] for row in range(m)]
for i in range(m):
    for j in range(n):
        arr[i][j] = i * j
print(arr)

# 12:
lines = list()
while True:
    line = input('Enter line (blank line to terminate): ')
    line = line.lower()
    lines.append(line)
    if line == '':
        break
for i in lines:
    print(i)

# 13:
numbers = input('Enter a sequence of 4 digit binary numbers: ')
numbers = numbers.split(',')
item = []
for n in numbers:
    if int(n, 2) % 5 == 0:  # int(value, base)
        item.append(n)
        print(','.join(item))

# 14:
string = input('Enter a string: ')
digits = 0
letters = 0
for i in string:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
print('Letters:', letters)
print('Digits:', digits)

# 15:
password = input('Enter password: ')
lower = 0
upper = 0
number = 0
char = ['$', '#', '@']
special = 0
if 6 <= len(password) <= 16:
    for i in password:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            number += 1
        elif i in char:
            special += 1
    if lower >= 1 and upper >= 1 and number >= 1 and special >= 1:
        print('Valid password')
    else:
        print('Invalid password')
else:
    print('Password must have 6 - 16 characters')

# 16 Solution 1:
num_list = [str(n) for n in range(100, 401)]
num = []
for number in num_list:
    count = 0
    for digit in number:
        if int(digit) % 2 == 0:
            count += 1
    if count == 3:
        num.append(number)
print(','.join(num))

# 16 Solution 2:
num_list = []
for number in range(100, 401):
    number = str(number)
    if int(number[0]) % 2 == 0 and int(number[1]) % 2 == 0 and int(number[2]) % 2 == 0:
        num_list.append(number)
print(','.join(num_list))

# 17 - 30: print pattern
blank = ' '
pattern = '*'
# 17: A
for row in range(7):
    for col in range(5):
        if (row == 0 or row == 3) and col != 0 and col != 4:
            print(pattern, end='')
        elif row != 0 and (col == 0 or col == 4):
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 18: D
for row in range(7):
    for col in range(5):
        if (row == 0 or row == 6) and col != 4:
            print(pattern, end='')
        elif row != 0 and row != 6 and (col == 0 or col == 4):
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 19: E
for row in range(7):
    for col in range(5):
        if col == 0:
            print(pattern, end='')
        elif row == 3 and col == 4:
            print(blank, end='')
        elif row == 0 or row == 3 or row == 6:
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 20: G
for row in range(7):
    for col in range(5):
        if (row == 0 or row == 6) and (col == 1 or col == 2 or col == 3):
            print(pattern, end='')
        elif row == 2 and col == 4:
            print(blank, end='')
        elif row != 0 and row != 6 and (col == 0 or col == 4):
            print(pattern, end='')
        elif row == 3 and (col == 2 or col == 3):
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 21: L
for row in range(7):
    for col in range(5):
        if col == 0:
            print(pattern, end='')
        elif row == 6:
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 22: M
for row in range(7):
    for col in range(5):
        if col == 0 or col == 4:
            print(pattern, end=' ')
        elif row == 2 and (col == 1 or col == 3):
            print(pattern, end=' ')
        elif row == 3 and col == 2:
            print(pattern, end=' ')
        else:
            print(blank, end=' ')
    print('')
# 23: O
for row in range(7):
    for col in range(5):
        if row != 0 and row != 6 and (col == 0 or col == 4):
            print(pattern, end='')
        elif (row == 0 or row == 6) and col != 0 and col != 4:
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 24: P
for row in range(7):
    for col in range(5):
        if (row == 0 or row == 3) and col != 4:
            print(pattern, end='')
        elif col == 0:
            print(pattern, end='')
        elif (row == 1 or row == 2) and col == 4:
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 25: R
for row in range(7):
    for col in range(5):
        if (row == 0 or row == 3) and col != 4:
            print(pattern, end='')
        elif col == 0:
            print(pattern, end='')
        elif (row == 1 or row == 2 or row == 6) and col == 4:
            print(pattern, end='')
        elif (row == 4 and col == 2) or (row == 5 and col == 3):
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 26: S
for row in range(7):
    for col in range(5):
        if (row == 0 or row == 3 or row == 6) and col != 0 and col != 4:
            print(pattern, end='')
        elif (row == 1 or row == 2 or row == 6) and col == 0:
            print(pattern, end='')
        elif (row == 0 or row == 4 or row == 5) and col == 4:
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 27: T
for row in range(7):
    for col in range(5):
        if row == 0:
            print(pattern, end='')
        elif col == 2:
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 28: U
for row in range(7):
    for col in range(5):
        if row == 6 and col != 0 and col != 4:
            print(pattern, end='')
        elif (col == 0 or col == 4) and row != 6:
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 29: X
for row in range(7):
    for col in range(7):
        if (col == 1 or col == 3) and (row == 2 or row == 4):
            print(pattern, end='')
        elif (col == 0 or col == 4) and row != 2 and row != 3 and row != 4:
            print(pattern, end='')
        elif col == 2 and row == 3:
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 30: Z
for row in range(7):
    for col in range(7):
        if row == 0 or row == 6:
            print(pattern, end='')
        elif (row == 1 and col == 5) or (row == 2 and col == 4) or (row == 3 and col == 3) or (row == 4 and col == 2) or (row == 5 and col == 1):
            print(pattern, end='')
        else:
            print(blank, end='')
    print('')
# 31:
year = int(input("Enter a dog's age in human years: "))
if year <= 2:
    age = year * 10.5
else:
    age = 2 * 10.5 + (year - 2) * 4
print("The dog's age in dog's years:", int(age))

# 32:
alphabet = input("Enter an alphabet: ")
vowels = ['a', 'e', 'i', 'o', 'u']
if alphabet in vowels:
    print(alphabet, 'is a vowel')
else:
    print(alphabet, 'is a consonant')

# 33:
m30days = ['April', 'June', 'September', 'September', 'November']
m31days = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month = input('Enter the name of Month: ')
if month in m30days:
    print('Number of days: 30 days')
elif month in m31days:
    print('Number of days: 31 days')
elif month == 'February':
    print('Number of days: 28/29 days')
else:
    print('Wrong Month name')

# 34:
a = int(input('Enter integer a: '))
b = int(input('Enter integer b: '))
Sum = a + b
if 15 <= Sum <= 20:
    print('Sum = 20')
else:
    print('Sum =', Sum)

# 35:
string = input("Enter a string: ")
try:
    number = int(string)
    print(number, 'is an integer')
except:
    print(string, 'is not an integer')

# 36:
print('Enter lengths of the triangle sides: ')
x = float(input('x = '))
y = float(input('y = '))
z = float(input('z = '))
if x == y == z:
    print('Equilateral triangle')
elif x == y or x == z or y == z:
    print('Isosceles triangle')
else:
    print('Scalene triangle')
# 37 đề lỗi
# 38:
day = int(input('Enter birthday: '))
month = input('Enter month of birthday: ')
if month == 'december':
    astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
elif month == 'january':
    astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
elif month == 'february':
    astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
elif month == 'march':
    astro_sign = 'Pisces' if (day < 21) else 'Aries'
elif month == 'april':
    astro_sign = 'Aries' if (day < 20) else 'Taurus'
elif month == 'may':
    astro_sign = 'Taurus' if (day < 21) else 'Gemini'
elif month == 'june':
    astro_sign = 'Gemini' if (day < 21) else 'Cancer'
elif month == 'july':
    astro_sign = 'Cancer' if (day < 23) else 'Leo'
elif month == 'august':
    astro_sign = 'Leo' if (day < 23) else 'Virgo'
elif month == 'september':
    astro_sign = 'Virgo' if (day < 23) else 'Libra'
elif month == 'october':
    astro_sign = 'Libra' if (day < 23) else 'Scorpio'
elif month == 'november':
    astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
else:
    astro_sign = ''
print("Your Astrological sign is :", astro_sign)

# 40:
a = float(input('Input first number: '))
b = float(input('Input second number: '))
c = float(input('Input third number: '))
if a > b:
    if b > c:  # a > b > c
        median = b
    elif a > c:  # a > c > b
        median = c
    else:  # c > a > b
        median = a
else:  # a < b
    if b < c:  # c > b > a
        median = b
    elif a < c:   # b > c > a
        median = c
    else:  # b > a > c
        median = a
print("The median is", median)

# 41:
def leapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    elif year % 400 == 0:
        return True
    else:
        return False

year = int(input('Input a year: '))
month = int(input('Input a month [1-12]: '))
day = int(input('Input a day [1 - 31]: '))
m31days = [1, 3, 5, 7, 8, 10, 12]
m30days = [4, 6, 9, 11]
if 0 < month <= 12 and 0 < day <= 31:
    if month == 12 and day == 31:
        year += 1
        month = 1
        day = 1
    elif month in m31days and day == 31:
        month += 1
        day = 1
    elif month in m30days and day == 30:
        month += 1
        day = 1
    elif month == 2 and day == 28:
        if leapyear(year):
            day += 1
        else:
            month += 1
            day = 1
    elif month == 2 and day == 29:
        if leapyear(year):
            month += 1
            day = 1
        else:
            print('This is not leap year. So the output is incorrect.')
    else:
        day += 1
    print(f'The next date is [yyyy-mm-dd]: {year}-{month}-{day}')
else:
    print('Wrong month or day')

# 42:
def calculate(numlist):
    Sum = 0
    for n in numlist:
        Sum += n
    print('Sum: ', Sum)
    print('Average: ', Sum/(len(numlist)-1))

numlist = []
while True:
    number = int(input('Enter integer: '))
    numlist.append(number)
    if number == 0:
        calculate(numlist)
        break

# 43:
number = int(input('Enter a number: '))
for n in range(1, 11):
    product = number * n
    print(f'{number} x {n} = {product}')

# 44:
num = 1
for i in range (1, 10):
    for j in range(i):
        print(num, end='')
    print('')
    num += 1

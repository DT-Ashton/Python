def binarytodecimal(binary):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    print(decimal, end=' ')

numbers = input('Enter a sequence of 4 digit binary numbers: ')
numbers = numbers.split(',')
for n in numbers:
    binarytodecimal(int(n))

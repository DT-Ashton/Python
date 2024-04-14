def print_table(n):
    i = 1
    while i <= 10:
        print(i, 'x', n, '=', i*n)
        i = i + 1

while True:
    n = int(input('Enter n: '))
    if 1 < n <= 9:
        print_table(n)
        break

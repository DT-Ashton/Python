# Nhập vào 3 số a, b, c:
a = float(input('Enter real number a: '))
b = float(input('Enter real number b: '))
c = float(input('Enter real number c: '))
# Xếp theo thứ tự tăng dần:
maximum = a
minimum = 0
middle = 0
# Giả sử a là max
if maximum < b:
    maximum = b
    if maximum < c:
        maximum = c
        minimum = a
        middle = c
    elif a < c:
        minimum = a
        middle = c
    else:
        minimum = c
        middle = a
elif maximum < c:
    maximum = c
    minimum = b
    middle = a
elif b < c:
    minimum = b
    middle = c
else:
    minimum = c
    middle = b
print('The maximum value among them is:', maximum)
print('The minimum value among them is:', minimum)
print(minimum, '<=', middle, '<=', maximum)

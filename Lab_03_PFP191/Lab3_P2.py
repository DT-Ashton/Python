line = str(input('Enter some characters: '))
letters = digits = others = 0
for i in line:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
    else:
        others += 1
print('Number of digits:', digits)
print('Number of letters:', letters)
print('Number of other keys:', others)

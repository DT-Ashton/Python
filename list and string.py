#string:
line = 'pls have a nice day'
print(line.startswith('pls'))
print(line.startswith('have'))

fruit = 'banana monkey'
count = 0
for letter in fruit:
    print(letter)
    if letter == 'a':
        count += 1
print(count)

print(fruit[2:6])
print(fruit[7:])
print(fruit[:3])
print(fruit[:])

s = ['hello','dt','bacon']
for i in [5,3,1,'a','b','c']:
    print(i)

a = ['hello','dt','bacon']
print(a)
a[2] = 'ashton'
print(a)

#kết hợp list và string:
#Danh sách sinh viên học AI:
mssv = str(input("Nhap danh sach ma so sinh vien ngan cach bang dau ',': "))
danhsach = mssv.split(',')  # lúc này danhsach dưới dạng list
print(danhsach)
print('Danh sach sv nganh AI:')
for line in danhsach:
    line = line.strip()
    if line[0:2] == 'AI':
        print(line)

#reversed sentence cách 1:
string = str(input('Enter a sentence: '))
Reversed = string.split()[::-1]
line = []
for i in Reversed:
    line.append(i)
print(' '.join(line))

#reversed sentence cách 2:
string = str(input('Enter a sentence: '))
reverse_sentence = string.split()
reverse_sentence.reverse()
for w in reverse_sentence:
    print(w, end=' ')

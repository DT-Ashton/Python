#1 Cách gọi 1:
bag = dict()
bag['tissues'] = 75
bag['money'] = 12
bag['notebooks'] = 5
print(bag)
print(bag['money'])

#2 Cách gọi 2:
n = {'dt': 1, 'bacon': 3, 'nick': 10}
print(n)
j = {}
print(j)

#3 Đếm số lần xuất hiện của các tên
counts = {'bacon': 1}
names = ['dt', 'bacon', 'nick', 'seal', 'grizzly', 'piggy']
for i in names:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] = counts[i] + 1  # cách 1
print('Counts: ', counts)

#4 đếm số từ xuất hiện trong câu văn/ đoạn văn:
counts2 = dict()
line = input('Enter a line: ')
words = line.split()
print('Words:', words)
for n in words:
    counts2[n] = counts2.get(n, 0) + 1  # cách 2(gọn hơn, khỏi if else)
print('Counts:',counts2)

#5 Danh sách sinh viên có họ tên và mssv:
student_list = dict()
for i in range(3):
    name = input("Enter student's full name: ")
    mssv = input('Enter mssv: ')
    student_list[name] = mssv
print('List of student with full names and mssv')
for a,b in student_list.items():  # .item() trả kết quả dưới dạng tuple
    print(a, '|', b)

#6 Concentrate dictionaries:
dic = {}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic.update(dic1)  # Mỗi câu lệnh chỉ kết hợp đc 1 cái
print(dic)
dic = dic1 | dic2 | dic3  # Kết hợp đc nhiều cái
print(dic)

#7 max/min value of a dictionary:
my_dict = {'x': 500, 'y': 5874, 'z': 560, 'a': 720, 'c': 3000}
print('Max value:', max(my_dict.values()))
print('Min value:', min(my_dict.values()))

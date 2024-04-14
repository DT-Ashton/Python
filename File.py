#1 Write a new file:
f = open('thu.txt.','w')
f.write('hi\n')
f.write('hello\n')
f.write('how are you today?')
f.close()

#2 Open and read an existed file:
fhand = open('thu.txt') #ko ghi gì đằng sau thì mặc định là 'r' 
nd = fhand.read()
print(nd)
print(len(nd))
fhand.seek(0) # chuyển con trỏ lên đầu
for i in fhand:
    i = i.rstrip()
    print(i)


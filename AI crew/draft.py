def heading(str):
    print("+++%s+++" % str)
heading.id = 1
heading.text = "Python functions"
heading("%d %s" % (heading.id, heading.text))

def printScores(student, *scores):
    print(f"Student Name: {student}")
    print(type(scores))
printScores("Jonathan",100, 'dt', 88, 92, 99)

nums = range(2, 50)
for i in range(2, 8):
    nums = list(filter(lambda x: x == i or x % i, nums))
print(nums)

a = 'Abc'
b = 'Abc'
print(a == b)

import string
s = string.ascii_lowercase
print("string ", s[2])


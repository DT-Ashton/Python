def square(numbers):
    sq = list()
    for n in numbers:
        n = n * n
        sq.append(n)
    print(sq)

def concentrate(list1, list2):
    new = list()
    for i in range(len(list1)):
        new.append(list1[i] + list2[i])
    print(new)

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    square(numbers)
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    concentrate(list1, list2)

if __name__ == '__main__':
    main()

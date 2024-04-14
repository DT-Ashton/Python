def main():
    num_list = list()
    try:
        while True:
            number = int(input('Enter positive integer: '))
            num_list.append(number)
            if number == 0:
                break
        num_list.sort()
        for num in num_list:
            print(num, end=' ')
    except:
        print('Invalid input. Try again.')

if __name__ == "__main__":
    main()

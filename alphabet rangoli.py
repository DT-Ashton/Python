import string
alphabet = string.ascii_lowercase


def print_rangoli(size):
    # your code goes here
    bucket = "".join(alphabet[:size][::-1])
    number_of_digits = 2 * (2 * size - 1) - 1

    # Forward pass
    for i in range(size):
        print("-".join(bucket[:i + 1] + bucket[:i][::-1]).center(number_of_digits, "-"))

    # Reverse pass
    for i in range(size - 1, 0, -1):
        print("-".join(bucket[:i - 1] + bucket[:i][::-1]).center(number_of_digits, "-"))

if __name__ == '__main__':
    n = int(input('Enter size of rangoli: '))
    print_rangoli(n)
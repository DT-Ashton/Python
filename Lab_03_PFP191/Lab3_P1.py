import random

print('Dice Thrower\n============ ')
sought = int(input('Total sought: '))
n = 1
while True:
    dice = [random.randint(1, 6), random.randint(1, 6)]
    print('Result of throw', n, ':', dice[0], '+', dice[1])
    if sum(dice) == sought:
        print('You got your total in', n, 'throws!')
        break
    n = n + 1

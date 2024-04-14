def write_dict(animal):
    file = open('animal.txt', 'w')
    for eng, viet in animal.items():
        file.write('%s: %s\n' % (eng, viet))
    file.close()

def main():
    animal = {
        'dog': 'cho',
        'cat': 'meo',
        'hamster': 'chuot hamster',
        'gold fish': 'ca vang',
        'tropical fish': 'ca nhiet doi',
        'bird': 'chim',
        'rabbit': 'tho',
        'turtle': 'rua',
        'parrot': 'vet',
        'gecko': 'tac ke',
        'frog': 'ech',
        'ferret': 'chon suong',
        'snake': 'ran',
        'snail': 'oc sen',
        'Guinea pig': 'chuot lang'

    }
    write_dict(animal)

if __name__ == '__main__':
    main()

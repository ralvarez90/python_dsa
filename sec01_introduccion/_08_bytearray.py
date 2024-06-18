"""BYTEARRAY

Son secuencias de enteros de 8 bits mutables. Es decir
cada elemento está en el rango 0 <= x <= 255.
"""
import random


def showExample01():
    # creating bytearray
    a = bytearray([12, 8, 25, 2])
    print('Creating bytearray:')
    print(a)

    # accessing elementos
    print('Accessing elements: ', a[1] if len(a) > 1 else None)

    # modifying elements
    if len(a) > 1:
        a[1] = 3
        print(a)

    # add elementos
    for _ in range(100):
        a.append(random.randint(0, 255))

    print(f'Final bytearray: {a}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')

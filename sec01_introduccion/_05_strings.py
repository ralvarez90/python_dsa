"""STRINGS

Son secuencias de bytes inmutables e instancias de 
la clase str. Cada elemento representa un caracter
unicode.

Python no cuenta con tipo caracteres, son strings de
longitud 1.
"""


def showExample01():
    # string instanca
    someStr = 'Welcome to Geeks for Geeks'
    print('Creating string: ')
    print(someStr)

    # printing first character
    if len(someStr) > 0:
        print('First character of string is: ')
        print(someStr[0])

    # pronting last character
    if len(someStr) > 0:
        print('Last character of string is: ')
        print(someStr[-1])


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')

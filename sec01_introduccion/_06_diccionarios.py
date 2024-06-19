"""DICCIONARIOS

Son colecciones no ordenadas que almacenan datos en pares
clave valor. Son indexados por medio de sus keys.
"""


def showExample01():
    # creating some dict
    someDict = {'name': 'Geeks', 1: [1, 2, 3, 4, 5]}
    print('Creating dictionary: ')
    print(someDict)

    # accessing a element using key
    print('Accessing a element using key: ')
    if 'name' in someDict.keys():
        print(f'someDict["name"] -> {someDict["name"]}')
        print(f'                 -> {someDict.get("name")}')

    # accessing using get method
    if 1 in someDict:
        print(f'someDict[1] -> {someDict.get(1, None)}')

    # creation using dictionary comprenhension
    otherDict = {x: x**2 for x in [1, 2, 3, 4, 5]}
    print(f'otherDict: {otherDict}')


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')

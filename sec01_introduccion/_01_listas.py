"""LISTAS

Son colecciones de datos mutables que permiten almacenar elementos de manera
indexada. Los elementos son indexados desde el 0 hasta el de su longitud - 1.
"""


def showExample01():
    someList = ['Geeks', 'For', 'Geeks']
    print(someList, 'with type:', type(someList))


def showExample02():
    someList = [['Geeks', 'For'], ['Geeks']]
    print(f'Size of items list: {len(someList)}')

    for sublist in someList:
        print(sublist)

    print(f'Last item in {someList}')
    print(someList[-1] if len(someList) > 0 else None)


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')

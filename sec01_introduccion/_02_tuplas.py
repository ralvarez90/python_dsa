"""
TUPLES

Son colecciones inmutables de datos. Son instancias de la clase
tuple. Las tuples y las listas son colecciones iterables por lo
que podemos hacer conversiones entre estos tipos de datos mediante
las clases tuple y list.
"""


def showExample01():
    someTuple = ('Geeks', 'For', 'Geeks')
    print(f'someTuple: {someTuple}')
    for item in someTuple:
        print(f'- {item}')


def showExample02():
    someSeq = ['Geeks', 'For', 'Geeks']
    print('Converting list in a tuple')
    someSeq = tuple(someSeq)
    print(type(someSeq))


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')

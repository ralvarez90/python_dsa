"""SETS

Son colecciones de elementos sin repetir. Son instancias
de la clase Set.
"""
import random


def showExample01():
    someItems = [random.randint(1, 10) for _ in range(10)]
    print(f'someItems has a type: f{someItems}')
    someItems = set(someItems)
    print(f'After deleting some items: {someItems}')


def showExample02():
    someSet = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
    print(f'someSet {someSet}, with type: {type(someSet)}')


def main():
    showExample01()
    showExample02()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')

"""FROZENSET

Son conjuntos inmutables. Es decir, una vez que se crean no
pueden cambiar de estado.

Notas:
- Un frozenset NO cumple la relación 'es un' set
"""


def showExample01():
    # normal set
    normalSet = set(['a', 'b', 'c'])
    print(f'normalSet: {normalSet}, with type {type(normalSet)}')

    # frozen set
    frozenSet = frozenset(['a', 'b', 'c'])
    print(f'frozenSet: {frozenset}, with type {type(frozenset)}')

    # test de tipo set
    print(isinstance(normalSet, set))
    print(isinstance(frozenSet, set))

    # test de tipo frozenset
    print(isinstance(normalSet, frozenset))
    print(isinstance(frozenSet, frozenset))


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')

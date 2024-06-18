"""MATRICES

Son arreglos multidimensionales, donde cada uno de sus elementos
tiene un mismo tamaño.

Para crear una matriz altamente eficiente contamos con bibliotecas
como numpy.
"""
import numpy as np


def showExample01():
    # create some numpy array
    arr = np.array([
        [1, 2, 3, 4],
        [4, 55, 1, 2],
        [8, 3, 20, 19],
        [11, 2, 22, 21],
    ])

    # matriz from np.array
    m = np.reshape(arr, (4, 4))
    print(m)

    # accessing elements
    print('\n\nAccessing elements:')
    print(arr[1])
    print(arr[2][0])

    # adding elements
    m = np.append(m, [[1, 15, 13, 11]], 0)
    print('\n\nAdding elements')
    print(m)

    # delete elemento
    m = np.delete(m, [1], 0)
    print('\nDeleting element:')
    print(m)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')

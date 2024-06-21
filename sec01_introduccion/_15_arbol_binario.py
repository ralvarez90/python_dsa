"""BINARY TREE

Un árbol binario es un árbol cuyos elementos pueden tener a lo más dos hijos. 
Dado que cada elemento de un árbol binario puede tener sólo 2 hijos, normalmente 
los llamamos hijos izquierdo y derecho. 

Un nodo de árbol binario contiene las siguientes partes.
- Un dato
- Apuntador al nodo hijo izquierdo
- Apuntador al nodo hijo derecho
"""
from typing import Any, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None


def showExample01():
    # create root
    root = Node(1)

    # 2 and 3 become left and right children of 1
    root.left = Node(2)
    root.right = Node(3)

    # 4 becomes left child of 2
    root.left.left = Node(4)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . . ')

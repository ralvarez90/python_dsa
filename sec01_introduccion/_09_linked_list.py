"""LISTAS LIGADAS

Estructura de datos lineal, de forma que cada uno de sus elementos no está
almacenado en espacios de memoria contigua. Cada elemento está enlazado o
ligado a otro mediante apuntadores.

Una lista enlazada está representada por un puntero al primer nodo de la
lista. El primer nodo se llama cabeza. Si la lista enlazada está vacía,
entonces el valor del encabezado es NULL.

Cada nodo de una lista consta de al menos dos partes:
- un dato
- un puntero (referecia) al siguiente nodo.
"""
from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None


# code execution
if __name__ == '__main__':

    # start with empty list
    llist = LinkedList()

    # set node not null in head
    llist.head = Node(1)

    # create more nodes
    second = Node(2)
    third = Node(3)

    # link first node with second
    llist.head.next = second

    # link second node with the third node
    second.next = third

    # end message
    input('\nPress any key to continue . . .')

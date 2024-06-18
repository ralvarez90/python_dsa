"""LINKED LIST
"""
from typing import Any


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


def showExample01():
    # start with the empty ll
    llist = LinkedList()

    # set head node in llist
    llist.head = Node(1)

    # create other nodes
    second = Node(2)
    third = Node(3)

    # assign next node in llist
    llist.head.next = second
    second.next = third

    # show llist
    llist.printList()


def main():
    showExample01()


# run application
if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')

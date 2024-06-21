"""PRIORITY QUEUE

Las colas de prioridad son estructuras de datos abstractas
donde cada dato/valor de la cola tiene una determinada
prioridad. Por ejemplo, en las aerolíneas el equipaje
con el título “Business” o “Primera clase” llega antes
que el resto.

Priority Queue es una extensión de la cola con las siguientes
propiedades:
- Un elemento con alta prioridad se retira de la cola antes
que un elemento con baja prioridad.
- Si dos elementos tienen la misma prioridad, se sirven
según su orden en la cola.
"""
from typing import TypeVar

# definición de tipo genérico
T = TypeVar('T')


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []

    # for checking if queue is empty
    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data: T) -> 'PriorityQueue':
        self.queue.append(data)
        return self

    # for popping an element based on priority
    def delete(self):
        try:
            # indice del valor máximo en lista
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i

            # dato máximo a retornar
            item = self.queue[max]

            # eliminación del dato en la cola
            del self.queue[max]
            return item
        except IndexError:
            print() or exit()

    def __str__(self) -> str:
        return ' '.join([str(_) for _ in self.queue])


def showExample01():

    # se crea instancia
    someQueue = PriorityQueue()

    # se agregan elementos
    someQueue       \
        .insert(12) \
        .insert(1)  \
        .insert(14) \
        .insert(7)  \

    # se muestra estado de la cola
    print(someQueue)

    # eliminamos elementos


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue. . . ')

"""HEAPS (MONTÍCULOS)

Un heap es una estructura de datos en forma de arbol binario ampliamente
utilizado en algoritmos de ordenamiento y en la implementación de
priority queues.

El módulo heapq en Python proporciona esta estructura de datos que se utiliza 
principalmente para representar una cola de prioridad. La propiedad de esta 
estructura de datos es que siempre proporciona el elemento más pequeño 
(min-heap) cada vez que se extrae el elemento. 


"""
import heapq


def showExample01():
    # lista inicial
    li = [5, 7, 9, 1, 3]
    print(f'li: {li}, with type: {type(li)}')

    # convertimos una lista en el heap
    heapq.heapify(li)

    # printing createad head
    print('The created heap is : ', end='')
    print(li)

    # using heappush to push elements into heap
    # pushes 4
    heapq.heappush(li, 4)

    # printint modified heap
    print('The modified heap after push is : ', end='')
    print(li)

    # using heappop to pop smallest element
    print(heapq.heappop(li))


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . . ')

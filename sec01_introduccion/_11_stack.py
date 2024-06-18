"""STACK (PILAS)

Son estructuras de datos lineales de tipo LIFO (Last input - First output).
Las funciones asociadas a un stack suelen ser:

empty
    Retorna si el stack es vacío    O(1)

size
    Retorna el tamaño del stack     O(1)

top
    Retorna la referencia al último elemento agregado
    el que está en el top.
    
push(a)
    Inserta un elemento en el topo del stack
    
pop()
    Elimina el último elemento agregado.
"""


def showExample01():
    # append function to push
    stack = []
    stack.append('G')
    stack.append('A')
    stack.append('Y')

    # initial stack
    print('Initial stack')
    print(stack)

    # pop function to pop last inserted element
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print('\nStack after elements are popped:')
    print(stack)


def main():
    showExample01()


if __name__ == '__main__':
    main()
    input('\nPress any key to continue . . .')

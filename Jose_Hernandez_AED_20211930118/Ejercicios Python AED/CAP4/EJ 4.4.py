from Deque import *

# Crear una cola doble con capacidad para 5 elementos
d = Deque(5)

# Insertar elementos en la cola doble
d.insertRight(1)
d.insertRight(5)
d.insertRight(9)

# Imprimir el contenido de la cola doble
print('Contenido de la cola doble:', end=' ')
for i in range(d.size):
    print(d.items[(d.front + i) % d.capacity], end=' ')
print()

# Insertar un elemento en la parte izquierda de la cola doble
d.insertLeft(0)


print('Contenido de la cola doble:', end=' ')
for i in range(d.size):
    print(d.items[(d.front + i) % d.capacity], end=' ')
print()

# Eliminar el elemento de la parte derecha de la cola doble
d.removeRight()


print('Contenido de la cola doble:', end=' ')
for i in range(d.size):
    print(d.items[(d.front + i) % d.capacity], end=' ')
print()

# Eliminar el elemento de la parte izquierda de la cola doble
d.removeLeft()


print('Contenido de la cola doble:', end=' ')
for i in range(d.size):
    print(d.items[(d.front + i) % d.capacity], end=' ')
print()


print('Primer elemento de la cola doble:', d.peekLeft())


print('Último elemento de la cola doble:', d.peekRight())


print('La cola doble está vacía?', d.isEmpty())


print('La cola doble está llena?', d.isFull())
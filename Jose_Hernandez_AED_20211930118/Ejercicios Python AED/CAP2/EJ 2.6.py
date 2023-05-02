import random

# Lista de letras del alfabeto
l= "abcdefghij"

# Crear el arreglo con índices alfabéticos y números aleatorios
arr = [(lk, random.randint(1, 20)) for lk in l]

# Imprimir el arreglo original
print("Arreglo original:")
print(arr)

def remove_repetidos(arr):
    # Crear un conjunto vacío para hacer un seguimiento de los valores únicos
    vu= set()

    # Crear una nueva lista para almacenar los elementos no duplicados
    nd = []

    # Recorrer el arreglo y agregar elementos no duplicados a la nueva lista
    for el in arr:
        # Si el valor aleatorio no está en el conjunto de valores únicos, agregar el elemento a la nueva lista
        if el[1] not in vu:
            nd.append(el)
            vu.add(el[1])
    
    # Devolver la nueva lista sin elementos duplicados
    return nd

# Eliminar los elementos duplicados del arreglo y mostrar el resultado
arr2 = remove_repetidos(arr)
print("Arreglo sin ningún elemento duplicado:")
print(arr2)

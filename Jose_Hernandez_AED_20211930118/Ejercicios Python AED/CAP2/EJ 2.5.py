import random

# Lista de letras del alfabeto
l= "abcdefghij"

# Crear el arreglo con índices alfabéticos y números aleatorios
arr = [(lk, random.randint(1, 20)) for lk in l]

# Imprimir el arreglo original
print("Arreglo original:")
print(arr)

# Método para combinar elementos con el mismo número aleatorio
def combinar(arr):
    # Crear un diccionario para agrupar elementos por número aleatorio
    g = {}
    for lk, n in arr:
        if n in g:
            g[n].append(lk)
        else:
            g[n] = [lk]
    # Crear una lista de elementos combinados
    combi = []
    for n, l in g.items():
        if len(l) > 1:
            combi.append((''.join(sorted(l)), n))
        else:
            combi.append((l[0], n))
    return combi

# Llamar al método para combinar elementos con el mismo número aleatorio
combi = combinar(arr)

# Imprimir el arreglo combinado
print("Arreglo con conjuntos combinados:")
print(combi)

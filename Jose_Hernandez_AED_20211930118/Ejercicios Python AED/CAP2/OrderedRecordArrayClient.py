import random

# Lista de letras del alfabeto
letras = "abcdefghij"

# Crear el arreglo con índices alfabéticos y números aleatorios
arreglo = [(letra, random.randint(1, 20)) for letra in letras]

# Imprimir el arreglo original
print("Arreglo original:")
print(arreglo)

# Método para combinar elementos con el mismo número aleatorio
def combinar(arreglo):
    # Crear un diccionario para agrupar elementos por número aleatorio
    grupos = {}
    for letra, numero in arreglo:
        if numero in grupos:
            grupos[numero].append(letra)
        else:
            grupos[numero] = [letra]
    # Crear una lista de elementos combinados
    combinados = []
    for numero, letras in grupos.items():
        if len(letras) > 1:
            combinados.append((''.join(sorted(letras)), numero))
        else:
            combinados.append((letras[0], numero))
    return combinados

# Llamar al método para combinar elementos con el mismo número aleatorio
combinados = combinar(arreglo)

# Imprimir el arreglo combinado
print("Arreglo combinado:")
print(combinados)

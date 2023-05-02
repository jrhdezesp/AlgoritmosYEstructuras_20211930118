class Node:
    def __init__(self, value, freq, left=None, right=None):
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right

def build_huffman_tree(data):
    # crea nodos iniciales
    nodes = [Node(key, value) for key, value in data.items()]
    while len(nodes) > 1:
        # ordena nodos por frecuencia
        ordered_nodes = sorted(nodes, key=lambda node: node.freq)
        # toma los dos nodos de menor frecuencia
        left = ordered_nodes[0]
        right = ordered_nodes[1]
        # crea el nodo padre
        parent = Node(left.value + right.value, left.freq + right.freq, left, right)
        # remueve los nodos hijos de la lista y agrega el nodo padre
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(parent)
    # el último nodo en la lista es el nodo raíz del árbol
    return nodes[0]

def generate_huffman_codes(node, code='', codes={}):
    if node.left is None and node.right is None:
        # es una hoja, guarda el código generado
        codes[node.value] = code
    else:
        # si no es hoja, genera el código para los hijos izquierdo y derecho
        generate_huffman_codes(node.left, code + '0', codes)
        generate_huffman_codes(node.right, code + '1', codes)
    return codes

def encode_huffman(message, codes):
    encoded_message = ''
    for char in message:
        if char in codes:
            # agrega el código para el carácter actual al mensaje codificado
            encoded_message += codes[char]
        else:
            raise ValueError(f'Character {char} not in codebook')
    return encoded_message

def decode_huffman(encoded_message, tree):
    decoded_message = ''
    current_node = tree
    for bit in encoded_message:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right
        if current_node.left is None and current_node.right is None:
            # se alcanzó una hoja, agrega el valor al mensaje decodificado y regresa al nodo raíz
            decoded_message += current_node.value
            current_node = tree
    return decoded_message

# Ejemplo de uso
data = {'a': 3, 'b': 6, 'c': 2, 'd': 1}
tree = build_huffman_tree(data)
codes = generate_huffman_codes(tree)

print('Codificación:')
message = 'abbcd'
print(f'Mensaje original: {message}')
encoded_message = encode_huffman(message, codes)
print(f'Mensaje codificado: {encoded_message}')

print('\nDecodificación:')
decoded_message = decode_huffman(encoded_message, tree)
print(f'Mensaje decodificado: {decoded_message}')

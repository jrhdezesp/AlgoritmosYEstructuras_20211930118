from BinarySearchTree import *


def main():
    bst = BinarySearchTree()

    # Inserción de nodos con claves duplicadas
    bst.insert(5, 'A')
    bst.insert(3, 'B')
    bst.insert(5, 'C')
    bst.insert(4, 'D')
    bst.insert(5, 'E')
    bst.insert(6, 'F')
    bst.insert(5, 'G')

    print(bst)  # 5:A:0,3:B:1,4:D:2,5:C:2,5:E:2,5:G:2,6:F:1

    # Eliminación del nodo con la clave 5 (último)
    bst.delete(5)
    print(bst)  # 5:A:0,3:B:1,4:D:2,5:C:2,5:E:2,6:F:1,5:G:2


if __name__ == '__main__':
    main()


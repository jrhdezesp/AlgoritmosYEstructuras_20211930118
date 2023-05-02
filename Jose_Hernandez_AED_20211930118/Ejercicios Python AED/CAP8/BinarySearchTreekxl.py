class BinarySearchTree:
    class _Node:
        def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right
            self.height = 1
            self.size = 1

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def __len__(self):
        return self._len(self._root)

    def _len(self, node):
        if node is None:
            return 0
        return node.size

    def __getitem__(self, key):
        node = self._get_node(key, self._root)
        if node is None:
            raise KeyError(str(key) + " not found")
        return node.value

    def _get_node(self, key, node):
        if node is None:
            return None
        elif key < node.key:
            return self._get_node(key, node.left)
        elif key > node.key:
            return self._get_node(key, node.right)
        else:
            return node

    def __setitem__(self, key, value):
        self._root = self._set_item(key, value, self._root)

    def _set_item(self, key, value, node):
        if node is None:
            return self._Node(key, value)
        elif key < node.key:
            node.left = self._set_item(key, value, node.left)
        elif key > node.key:
            node.right = self._set_item(key, value, node.right)
        else:
            node.value = value
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        node.size = 1 + self._len(node.left) + self._len(node.right)
        return self._balance(node)

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _balance(self, node):
        if self._balance_factor(node) < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
        elif self._balance_factor(node) > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
        return node
    
    def _node_balance(self, node):
        """
        Computes the number of nodes in the right subtree minus the number of nodes in the left subtree
        """
        if node is None:
            return 0
        return self._len(node.right) - self._len(node.left)

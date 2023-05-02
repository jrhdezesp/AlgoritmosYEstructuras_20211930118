class BinarySearchTree:
    class _Node:
        __slots__ = '_element', '_left', '_right', '_size', '_depth'
        def __init__(self, element, parent=None):
            self._element = element
            self._left = None
            self._right = None
            self._size = 1
            self._depth = 0
            self._parent = parent

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def __len__(self):
        return self._size(self._root)

    def size(self, node):
        if node is None:
            return 0
        return node._size

    def depth(self, node):
        if node is None:
            return -1
        return node._depth

    def _update_size(self, node):
        if node is None:
            return
        node._size = 1 + self.size(node._left) + self.size(node._right)
        self._update_size(node._parent)

    def _update_depth(self, node):
        if node is None:
            return
        node._depth = 1 + max(self.depth(node._left), self.depth(node._right))
        self._update_depth(node._parent)

    def __find(self, e):
        if self.is_empty():
            return None
        current = self._root
        while current is not None:
            if e == current._element:
                return current
            elif e < current._element:
                current = current._left
            else:
                current = current._right
        return None

    def search(self, e):
        node = self.__find(e)
        if node is None:
            return None
        return node._element

    def insert(self, e):
        if self.is_empty():
            self._root = self._Node(e)
            return
        parent = None
        current = self._root
        while current is not None:
            if e < current._element:
                parent = current
                current = current._left
            else:
                parent = current
                current = current._right
        new_node = self._Node(e, parent=parent)
        if e < parent._element:
            parent._left = new_node
        else:
            parent._right = new_node
        self._size += 1
        self._update_size(new_node)
        self._update_depth(new_node)

    def delete(self, e):
        node = self.__find(e)
        if node is None:
            return None
        if node._right is not None:
            # replace with smallest from the right subtree
            replace = node._right
            while replace._left is not None:
                replace = replace._left
        elif node._left is not None:
            # replace with largest from the left subtree
            replace = node._left
            while replace._right is not None:
                replace = replace._right
        else:
            replace = None

        if replace is not None:
            node._element = replace._element
            node = replace

        parent = node._parent
        if node._left is not None:
            child = node._left
        else:
            child = node._right
        if child is not None:
            child._parent = parent
        if parent is None:
            self._root = child
        elif node == parent._left:
            parent._left = child
       

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self) == 0

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2*i + 1

    def right_child(self, i):
        return 2*i + 2

    def get(self, i):
        return self.heap[i]

    def get_priority(self, i):
        return self.heap[i][0]

    def get_item(self, i):
        return self.heap[i][1]

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, priority, item):
        # Agrega el nuevo elemento al final del heap
        self.heap.append((priority, item))
        # Reordena el heap desde abajo hacia arriba para mantener la propiedad del heap
        i = len(self.heap) - 1
        while i > 0 and self.get_priority(i) < self.get_priority(self.parent(i)):
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def remove(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        # Guarda el elemento con mayor prioridad
        highest_priority_item = self.get_item(0)
        # Reemplaza el elemento con mayor prioridad por el último elemento del heap
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        # Reordena el heap desde arriba hacia abajo para mantener la propiedad del heap
        i = 0
        while (self.left_child(i) < len(self) and
               self.get_priority(i) > self.get_priority(self.left_child(i))) or \
              (self.right_child(i) < len(self) and
               self.get_priority(i) > self.get_priority(self.right_child(i))):
            if (self.right_child(i) < len(self) and
                self.get_priority(self.right_child(i)) < self.get_priority(self.left_child(i))):
                self.swap(i, self.right_child(i))
                i = self.right_child(i)
            else:
                self.swap(i, self.left_child(i))
                i = self.left_child(i)
        # Retorna el elemento con mayor prioridad
        return highest_priority_item

    def __str__(self):
        return str(self.heap)

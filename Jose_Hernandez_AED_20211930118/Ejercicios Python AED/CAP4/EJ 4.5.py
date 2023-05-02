from PriorityQueue import *
def test_priority_queue():
    queue = PriorityQueue()
    
    # Casos de prueba con inserciones en orden de prioridad
    queue.insert(0, 'Ada')
    queue.insert(1, 'Don')
    queue.insert(2, 'Tim')
    queue.insert(0, 'Joe')
    queue.insert(1, 'Len')
    queue.insert(2, 'Sam')
    queue.insert(0, 'Meg')
    queue.insert(0, 'Eva')
    queue.insert(1, 'Kai')
    assert str(queue) == "[(0, 'Ada'), (0, 'Joe'), (0, 'Meg'), (0, 'Eva'), (1, 'Don'), (1, 'Len'), (1, 'Kai'), (2, 'Tim)]"

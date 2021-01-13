class Queue:

    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity

    def enqueue(self, item):
        self.items.insert(0, item) if len(self.items) < self.capacity else None

    def dequeue(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def is_full(self):
        return len(self.items) == self.capacity



k = Queue(5)
k.enqueue(1)
k.enqueue(2)
k.enqueue(3)
k.enqueue(4)
k.enqueue(5)
k.enqueue(6)
print(k.items)
print(k.peek())
print(k.is_empty())
print(k.size())
print(k.is_full())


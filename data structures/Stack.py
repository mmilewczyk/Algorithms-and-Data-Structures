class Stack:

    def __init__(self):
        self.top = None
        self.height = 0

    def push(self, data):
        new_top = Element(data, self.top)
        self.top = new_top
        self.height += 1
        return self.top

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data

    def pop(self):
        if self.peek() is None:
            return None
        else:
            old_top = self.top
            self.top = old_top.predecessor
            self.height -= 1
            return old_top.data

    def clear(self):
        while self.height != 0:
            self.top = None
            self.height -= 1

    def is_empty(self):
        return self.height == 0


class Element:
    def __init__(self, data, predecessor):
        self.predecessor = predecessor
        self.data = data


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
stack.pop()
print(stack.peek())
stack.clear()
print(stack.is_empty())
print(stack.peek())



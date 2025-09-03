class Stack:
    def __init__(self, max_size=7):
        self.max_size = max_size
        self.items = []
    
    def push(self, x):
        if len(self.items) >= self.max_size:
            print("Error: Stack overflow")
            return
        self.items.append(x)
    
    def pop(self):
        if self.is_empty():
            print("Error: Stack underflow")
            return None
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0

stack = Stack()
stack.push(15)
stack.push(9)
print(stack.pop())
stack.push(7)
stack.push(14)
stack.push(1)
print(stack.pop())
print(stack.pop())
stack.push(3)
stack.push(18)

print(stack.items) 
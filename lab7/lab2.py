class Queue:
    def __init__(self, max_size=7):
        self.max_size = max_size
        self.items = []
    
    def enqueue(self, x):
        if len(self.items) >= self.max_size:
            print("Error: Queue overflow")
            return
        self.items.append(x)
    
    def dequeue(self):
        if self.is_empty():
            print("Error: Queue underflow")
            return None 
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0

queue = Queue()
queue.enqueue(21)
queue.enqueue(8)
queue.enqueue(15)
print(queue.dequeue()) 
queue.enqueue(6)
queue.enqueue(1)
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(27)
queue.enqueue(10)

print(queue.items) 
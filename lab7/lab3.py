class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()  
        self.head.next = self.head 
        self.head.prev = self.head

    def insert(self, k):
        new_node = Node(k)
        new_node.next = self.head.next
        new_node.prev = self.head
        
        self.head.next.prev = new_node
        self.head.next = new_node

    def search(self, k):
        current = self.head.next
        while current != self.head and current.key != k:
            current = current.next
        return current if current != self.head else None

    def delete(self, k):
        node_to_delete = self.search(k)
        if node_to_delete is not None:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    def display(self):
        current = self.head.next
        elements = []
        while current != self.head:
            elements.append(current.key)
            current = current.next
        print("Elements in the list:", elements)
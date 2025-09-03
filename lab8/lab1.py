class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def traverse(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node


head = None
head = insert_at_beginning(head, 4)
head = insert_at_beginning(head, 3)
head = insert_at_beginning(head, 2)
head = insert_at_beginning(head, 1)
traverse(head)
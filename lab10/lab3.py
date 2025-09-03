class Node:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

def right_rotate(tree, x):
    y = x.left
    x.left = y.right

    if y.right:
        y.right.parent = x

    y.parent = x.parent

    if not x.parent:
        tree.root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y

    y.right = x
    x.parent = y
    x.color, y.color = y.color, x.color


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix +
              str(node.key) + " (" + node.color + ")")
        print_tree(node.left, level + 1, "L--- ")
        print_tree(node.right, level + 1, "R--- ")

def create_sample_rb_tree():
    root = Node(10, "black")
    root.left = Node(5, "red", parent=root)
    root.right = Node(15, "red", parent=root)
    root.left.left = Node(3, "black", parent=root.left)
    root.left.right = Node(7, "black", parent=root.left)
    root.right.left = Node(20, "black", parent=root.right)
    root.right.right = Node(25, "black", parent=root.right)

    return root

rb_tree = create_sample_rb_tree()

print("Исходное дерево:")
print_tree(rb_tree)

right_rotate(rb_tree, rb_tree.left)

print("\nДерево после правого поворота:")
print_tree(rb_tree)
class BinaryTree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printTree(self, x=0):
        if self.left:
            self.left.printTree(x + 1)
        print(f'{x} -', self.data)
        if self.right:
            self.right.printTree(x + 1)
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

def fillTree(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = BinaryTree(arr[mid])
    root.left = fillTree(arr[:mid])
    root.right = fillTree(arr[mid + 1:])
    return root

def build_trees():
    keys = [1, 2, 4, 5, 7, 8, 9, 12]
    trees = {}
    
    tree_height_3 = fillTree(keys[:4]) 
    trees['высота_3'] = tree_height_3
    
    tree_height_4 = fillTree(keys)  
    trees['высота_4'] = tree_height_4

    unbalanced_keys = [1, 1, 2, 2, 4, 5, 7, 8, 9, 12]
    tree_height_6 = fillTree(unbalanced_keys)
    trees['высота_6'] = tree_height_6
    
    return trees

trees = build_trees()

for height, tree in trees.items():
    print(f"\n{height}:")
    tree.printTree()
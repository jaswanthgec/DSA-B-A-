class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.value == key:
        return root
    if root.value < key:
        return search(root.right, key)
    return search(root.left, key)

# Example usage:
root = None
keys = [20, 8, 22, 4, 12, 10, 14]

for key in keys:
    root = insert(root, key)

key_to_search = 10
result = search(root, key_to_search)
if result is not None:
    print(f"Element {key_to_search} found in BST.")
else:
    print(f"Element {key_to_search} not found in BST.")

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# In-order traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

# Pre-order traversal
def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

# Post-order traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

# Example Usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order traversal: ", end='')
inorder(root)
print("\nPre-order traversal: ", end='')
preorder(root)
print("\nPost-order traversal: ", end='')
postorder(root)

class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1

def get_height(root):
    if not root:
        return 0
    return root.height

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)

def insert_avl(root, key):
    if not root:
        return AVLNode(key)
    if key < root.val:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)
    
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)
    
    if balance > 1 and key < root.left.val:
        return right_rotate(root)
    if balance < -1 and key > root.right.val:
        return left_rotate(root)
    if balance > 1 and key > root.left.val:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and key < root.right.val:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    
    return root

# Example Usage
root = None
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = insert_avl(root, key)

print("AVL tree created with the given keys")

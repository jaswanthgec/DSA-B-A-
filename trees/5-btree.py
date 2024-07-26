class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []

def split_child(x, i, y):
    t = y.t
    z = BTreeNode(t, y.leaf)
    x.children.insert(i + 1, z)
    x.keys.insert(i, y.keys[t - 1])
    z.keys = y.keys[t: (2 * t - 1)]
    y.keys = y.keys[0: (t - 1)]
    if not y.leaf:
        z.children = y.children[t: (2 * t)]
        y.children = y.children[0: (t - 1)]

def insert_non_full(x, k):
    if x.leaf:
        i = len(x.keys) - 1
        x.keys.append(0)
        while i >= 0 and k < x.keys[i]:
            x.keys[i + 1] = x.keys[i]
            i -= 1
        x.keys[i + 1] = k
    else:
        i = len(x.keys) - 1
        while i >= 0 and k < x.keys[i]:
            i -= 1
        i += 1
        if len(x.children[i].keys) == 2 * x.t - 1:
            split_child(x, i, x.children[i])
            if k > x.keys[i]:
                i += 1
        insert_non_full(x.children[i], k)

def insert_btree(root, k, t):
    if len(root.keys) == 2 * t - 1:
        s = BTreeNode(t)
        s.children.append(root)
        split_child(s, 0, root)
        insert_non_full(s, k)
        return s
    else:
        insert_non_full(root, k)
        return root

# Example Usage
t = 3  # Minimum degree
root = BTreeNode(t, True)
keys = [10, 20, 5, 6, 12, 30, 7, 17]
for key in keys:
    root = insert_btree(root, key, t)

print("B-Tree created with the given keys")

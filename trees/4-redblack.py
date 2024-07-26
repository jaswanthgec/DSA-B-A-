from bintrees import RBTree

# Example Usage
rbt = RBTree()
keys = [20, 15, 25, 10, 5]
for key in keys:
    rbt.insert(key, key)

# Search for a key
key = 15
if rbt.get(key):
    print(f"Key {key} found in the Red-Black Tree")
else:
    print(f"Key {key} not found in the Red-Black Tree")

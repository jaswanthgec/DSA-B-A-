class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for (k, v) in self.table[index]:
            if k == key:
                return v
        return None

# Example usage:
hash_table = HashTable(10)
hash_table.insert(10, "Value10")
hash_table.insert(20, "Value20")
hash_table.insert(30, "Value30")

key_to_search = 20
result = hash_table.search(key_to_search)
if result is not None:
    print(f"Element with key {key_to_search} found: {result}.")
else:
    print(f"Element with key {key_to_search} not found.")

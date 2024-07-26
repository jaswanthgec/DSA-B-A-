class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.indexes = []

class SuffixTree:
    def __init__(self, text):
        self.root = SuffixTreeNode()
        self.text = text
        self.build_suffix_tree()

    def build_suffix_tree(self):
        for i in range(len(self.text)):
            suffix = self.text[i:]
            self._insert_suffix(suffix, i)

    def _insert_suffix(self, suffix, index):
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTreeNode()
            node = node.children[char]
            node.indexes.append(index)

    def search(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.indexes

# Example Usage
text = "banana"
suffix_tree = SuffixTree(text)

# Search for a pattern
pattern = "ana"
indexes = suffix_tree.search(pattern)
print(f"Pattern '{pattern}' found at indexes:", indexes)

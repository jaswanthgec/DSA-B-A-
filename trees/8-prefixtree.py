class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

# Example Usage
trie = Trie()
words = ["hello", "world", "hi", "her"]
for word in words:
    trie.insert(word)

# Search for a word
search_word = "her"
if trie.search(search_word):
    print(f"Word '{search_word}' found in the Trie")
else:
    print(f"Word '{search_word}' not found in the Trie")

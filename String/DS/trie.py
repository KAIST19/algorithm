class Node():
    def __init__(self, key, data=None):
        self.key = key # the character
        self.data = data # the whole string
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        """
        insert the string to the trie
        """
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string
    
    def search(self, string):
        """
        string: string to search in the trie
        
        returns True if there is/False otherwise
        """
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        
        if current_node.data:
            return True
        else:
            return False
    
    def starts_with(self, prefix):
        """
        prefix: string to search in the trie
        returns a list of strings that starts with the prefix
        """
        current_node = self.head
        words = []
        
        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None
        
        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break
        
        return words
            

# Test
trie = Trie()
trie.insert("Hello")
trie.insert("Germany")
print(trie.search("Hello"))
print(trie.starts_with("R"))
print(trie.starts_with("G"))
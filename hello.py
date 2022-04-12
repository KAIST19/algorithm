class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
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
    

# Test
n, m = map(int, input().split())
trie = Trie()
for _ in range(n):
    trie.insert(input().rstrip())

cnt = 0
for _ in range(m):
    if trie.search(input().rstrip()):
        cnt += 1

print(cnt)
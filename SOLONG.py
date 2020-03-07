# 2020-3-7
# p 787
# incompleted

def toNumber(char: str) -> int:
    return ord(char) - ord("A")

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]

        # first word added to this node
        self.first = -1

        # id, if this node is terminal
        self.terminal = -1 
    
    def insert(self, key: str, id: int):
        if first == -1: first = id
        if len(key) == 0:
            self.terminal = id
        else:
            next = toNumber(key[0])
            if self.children[next] is None:
                self.children[next] = TrieNode()
            self.children[next].insert(key[1:], id)
    
    def find(self, key: str) -> TrieNode:
        if len(key) == 0:
            return self
        
        next = toNumber(key[0])
        if self.children[next] is None:
            return None
        else:
            return self.children[next].find(key[1:])
    
    def type(self, key: str, id: int):
        '''
        return the number of keys to type key whoose id is id
        '''
        if len(key) == 0:
            return 0

        if self.first == id:
            return 1
        
        next = toNumber(key[0])
        return 1 + self.children[next].type(key[1:], id)
    
    def countKeys(self, key: str):
        word = self.find(key)
        if word is None:
            return len(word)
        else:
            return self.type(key, word.terminal)

def solve():


solve()
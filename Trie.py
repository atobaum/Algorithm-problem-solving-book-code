# 2020-3-7
from typing import List

nAlphabet = 26

def toNum(char: str) -> int:
    n = ord(char)
    if n < ord('a'): return n - ord('A')
    else: return n - ord('a')

class TrieNode:
    '''
    data structure for strings
    '''
    def __init__(self):
        self.__children: List[TrieNode] = [None for _ in range(nAlphabet)]
        self.__terminal = 0
    
    def insert(self, key: str):
        if len(key) == 0:
            self.__terminal = 1
        else:
            next = toNum(key[0])
            if self.__children[next] is None:
                self.__children[next] = TrieNode()
            self.__children[next].insert(key[1:])
    
    def find(self, key: str) -> TrieNode:
        if len(key) == 0:
            return self
        else:
            next = toNum(key[0])
            if self.__children[next] is None:
                return None
            else:
                return self.find(key[1:])
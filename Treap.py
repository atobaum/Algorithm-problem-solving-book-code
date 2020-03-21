# p709
# Treap 구현
# 랜덤화된 우선순위로 만든 이진 검색 트리
# 부모의 우선순위 > 자식의 우선순위

import random
from typing import TypeVar

T = TypeVar('T')

class Node:
    def __init__(self, key: T) -> None:
        self.key: T = key
        self.priority: int = random.randint(1, 2**32)
        self.right: Node = None
        self.left: Node = None
        # 이 노드를 루드로 하는 서브트리의 크기
        self.size: int = 1
    
    def setLeft(self, node: Node) -> None:
        self.left = node
        self.calcSize()
    
    def setRight(self, node: Node) -> None:
        self.right = node
        self.calcSize()
    
    def calcSize(self) -> None:
        self.size = 1
        if self.left:
            self.size += self.left.size
        if self.right:
            self.size += self.right.size
    
    def split(self, key: T):
        '''
        return tuple of roots whoose key of elements are smaller/ larger than k
        '''
        if self.key < key:
            if self.right is None:
                return (self, None)
            else:
                (l, r) = self.right.split(key)
                self.setRight(l)
                return (self, r)
        else:
            if self.left is None:
                return (None, self)
            else:
                (l, r) = self.left.split(key)
                self.setLeft(r)
                return (l, self)

    def insert(self, node: Node) -> Node:
        if self.priority > node.priority:
            if self.key < node.key:
                if self.right is None:
                    self.setRight(node) 
                self.setRight(self.right.insert(node))
            else:
                if self.left is None:
                    self.setLeft(node) 
                self.setLeft(self.left.insert(node))
            return self
        else:
            (l, r) = self.split(node.key)
            node.setLeft(l)
            node.setRight(r)
            return node
    
    @staticmethod
    def merge(a: Node, b: Node):
        if a is None:
            return b
        if b is None:
            return a
        if a.priority < b.priority:
            b.setLeft(Node.merge(a, b.left))
            return b
        if a.priority > b.priority:
            a.setRight(Node.merge(a.right, b))
            return a

    def erase(self, k: T):
        if self.key == k:
            return Node.merge(self.left, self.right)
        elif self.key < k:
            if self.right is not None:
                self.setRight(self.right.erase(k))
        else:
            if self.left is not None:
                self.setLeft(self.left.erase(k))
        return self
    
    def print(self):
        print(f'p: {self.key}, k: {self.key}, s: {self.size}')
    
    def kth(self, k: int) -> Node:
        '''
        k번째 원소 출력. 0에서 시작.
        '''
        leftSize = 0
        if self.left is not None:
            leftSize += self.left.size
        if leftSize < k:
            if self.right is None:
                return None
            self.right.kth(k - leftSize - 1)
        elif leftSize == k:
            return self
        else:
            return self.left.kth(k)
    
    def countLessThan(self, k: T) -> int:
        if self.key == k:
            if self.left is None:
                return 0
            return self.left.size
        elif self.key < k:
            less = 1
            if self.left is not None:
                less += self.left.size
            if self.right is None:
                return less
            else:
                return less + self.right.countLessThan(k)
        else:
            if self.left is None:
                return 0
            else:
                return self.left.countLessThan(k)

def test():
    r = Node(random.randint(1, 200))
    for _ in range(10):
        r = r.insert(Node(random.randint(1,200)))
    

if __name__ == "__main__":
    test()
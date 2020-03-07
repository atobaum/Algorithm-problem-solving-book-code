class UnionFind:
    def __init__(self, num):
        self.__tree = [i for i in range(num)]
    
    def find(self, v):
        '''
        return root of v
        '''
        p = self.__tree[v]
        if p == v: return v
        else:
            root = self.find(p)
            self.__tree[v] = root
            return root
    
    def merge(self, v, u):
        r1 = self.find(v)
        r2 = self.find(u)
        self.__tree[r2] = r1
        return r1
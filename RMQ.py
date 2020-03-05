import sys 

class RMQ:
    '''
    Range Minimum Query
    '''

    def __init__(self, array = []):
        self.__a = array
        self.__n = len(array)
        self.__r = [0 for _ in range(self.__n*4)]
        self.__init(0, 0, self.__n-1)
        print(self.__r)

    def __init(self, node, left, right):
        '''
        node, index representing [left, right]
        '''
        print(node, left, right)
        if left == right:
            self.__r[node] = self.__a[left]
            # print(node, self.__r[node], left)
        else:
            mid = self.__mid(left, right)
            lMin = self.__init(node*2+1, left, mid)
            rMin = self.__init(node*2+2, mid+1, right)
            self.__r[node] = min(lMin, rMin)
        return self.__r[node]
    
    def __query(self, n, nl, nr, l, r):
        '''
        n is the index of r representing a[nl, nr]
        returns minimum of a[l, r]
        '''
        if nl > r or nr < l:
            return sys.maxsize
        elif nl >= l and nr <= r:
            return self.__r[n]
        else:
            mid = self.__mid(nl, nr)
            return min(self.__query(n*2+1, nl, mid, l, r), self.__query(n*2+2, mid+1, nr, l, r))
    
    def query(self, left, right):
        return self.__query(0, 0, self.__n-1, left, right)

    def __update(self, n, nl, nr, idx, newValue):
        '''
        update when a[index] is updated to newValue
        '''
        if nl > idx or nr < idx:
            return self.__r[n]
        elif nl == nr:
            self.__r[n] = newValue
            return newValue
        else:
            mid = self.__mid(nl, nr)
            self.__r[n] = min(self.__update(n*2+1, nl, mid, idx, newValue), self.__update(n*2+2, mid+1, nr, idx, newValue))
            return self.__r[n]
    
    def update(self, index, value):
        '''
        update A[index] = value
        '''
        self.__a[index] = value
        self.__update(0, 0, self.__n-1, index, value)

    def __mid(self, a: int, b:int) -> int:
        return int((a+b)/2)
    
    def getItem(self,i):
        return self.__a[i]
    
    def getNode(self, i):
        return self.__r[i]
    
    def length(self):
        return self.__n

if __name__ == '__main__':
    import showTree
    R = RMQ([4,1,2,3,5,6,2])
    lfn = lambda n: n*2+1 if n*2+1 < R.length()*3 else None
    rfn = lambda n: n*2+2 if n*2+2 < R.length()*3 else None
    vfn = lambda n: str(R.getNode(n))
    G = showTree.visualization(0, lfn, rfn, vfn)
    G.draw()

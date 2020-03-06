# p. 746
# 2020.3.7
import RMQ
from typing import List

def preprocess(fathers: List[int])-> List[List[int]]:
    child = [[] for _ in fathers]
    child.append([])
    for c, f in enumerate(fathers):
        child[f].append(c+1)
    return child

class FAMILYTREE:
    def __init__(self, fathers: str):
        self.__child = preprocess(list(map(int, fathers.split())))
        n = len(fathers) + 1
        self.__no2serial = [-1 for _ in range(n)]
        self.__serial2no = [-1 for _ in range(n)]
        self.__depth = [-1 for _ in range(n)]
        self.__firstTrip = [-1 for _ in range(n)]
        self.__trip = [] # preorder traverse sequence
        self.__nextSerial = 0
        self.__traverse(0, 0)
        self.__RMQ = RMQ.RMQ(self.__trip)
    
    def __traverse(self, here: int, depth: int):
        self.__no2serial[here] = self.__nextSerial
        self.__serial2no[self.__nextSerial] = here
        self.__nextSerial += 1
        self.__depth[here] = depth

        self.__firstTrip[here] = len(self.__trip)
        self.__trip.append(self.__no2serial[here])
        for c in self.__child[here]:
            self.__traverse(c, depth+1)
            self.__trip.append(self.__no2serial[here])

    def distance(self, u: int, v: int):
        ul = self.__firstTrip[u]
        vl = self.__firstTrip[v]
        if ul > vl:
            ul, vl = vl, ul
        rootSerial = self.__RMQ.query(ul, vl)
        lca = self.__serial2no[rootSerial]
        return self.__depth[u] + self.__depth[v] - 2* self.__depth[lca]
    
if __name__ == '__main__':
    f = FAMILYTREE("0 1 1 3 3 0 6 0 8 9 9 8")
    print(f.distance(2,7))
    print(f.distance(10,11))
    print(f.distance(4,11))
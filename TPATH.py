# 2020.3.22
# p981
# wrong
from utils import parse
inf = float('inf')

def test():
    inputs = """3
2 1
0 1 100
4 3
0 1 127
1 2 14
2 3 96
4 4
0 1 100
1 3 99
0 2 17
2 3 10"""
    inputs = parse(inputs)

    c, = inputs.pop()
    for _ in range(c):
        v, e = inputs.pop()
        adj = [[] for _ in range(v)]
        weights = []
        edges = []
        for _ in range(e):
            a, b, cost = inputs.pop()
            adj[a].append((b, cost))
            adj[b].append((a, cost))
            edges.append((cost, (a, b)))
            edges.append((cost, (b, a)))
            weights.append(cost)

        weights.sort()
        edges.sort()
        print(minWeightDiff(adj, weights, edges))

def minWeightDiff(adj, weights, edges):
    ret = inf
    for w in weights:
        # ret = min(ret, minUpperBound(adj, w) - w)
        ret = min(ret, kruskalMinUpperBound(w, adj, edges) - w)
    return ret

def kruskalMinUpperBound(low, adj, edges):
    class DisjointSet:
        def __init__(self, n):
            self.parent = [i for i in range(n)]
        def find(self, n):
            p = self.parent[n]
            if p == n:
                return p
            else:
                p = self.find(p)
                self.parent[n] = p
                return p
        
        def merge(self, a, b):
            self.parent[self.find(a)] = b

    ds = DisjointSet(len(adj))
    for edge in edges:
        if edge[0] < low: continue
        a = edge[1][0]
        b = edge[1][1]
        ds.merge(a, b)
        if ds.find(a) == ds.find(b):
            return edge[0]
    return inf

test()

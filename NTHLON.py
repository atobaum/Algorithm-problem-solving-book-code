# p936
# 2020.3.18
# Wrong
from dijkstra import Dijkstra

def solve(a, b):
    def d2v(diff):
        """
        return vertex number from score difference
        """
        return 200+diff

    n = len(a)
    startNode = 400
    adj = [[] for _ in range(401)]

    for idx in range(n):
        # cost is a's time
        adj[startNode].append((a[idx], a[idx] - b[idx]))
    
    for v in range(-199, 200):
        for idx in range(n):
            next = v + a[idx] - b[idx]
            if next < -199 or next > 199:
                continue
            adj[d2v(v)].append((a[idx], d2v(next)))
    
    dist = Dijkstra(adj, startNode)
    return dist[d2v(0)]

def test():
    inputs = """3
2
1 2
7 3
5
1 100
20 11
21 20
10 1
2 101
3
10 81
63 71
16 51"""

    inputs = inputs.split('\n')
    inputs = [list(map(int, line.split())) for line in inputs]
    inputs.reverse()

    c, = inputs.pop()
    for _ in range(c):
        m, = inputs.pop()
        a = []
        b = []

        for _ in range(m):
            tempa, tempb = inputs.pop()
            a.append(tempa)
            b.append(tempb)
        ret = solve(a, b)
        if ret < float('inf'):
            print(ret)
        else:
            print("IMPOSSIBLE")

test()
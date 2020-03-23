# 2020.3.21
# p979

def solve(adj):
    inf = float('inf')
    selected = []
    res = 0
    n = len(adj)
    # 해당 정점이 트리에 포함 여부
    added = [False] * n
    # 트리에 인접한 최소 cost
    minWeight = [inf] * n
    parent = [None] * n

    minWeight[0] = 0
    parent[0] = 0

    for _ in range(n):
        # 다음 추가할 정점
        u = None
        # 추가할 정점 찾기
        for i in range(n):
            if (not added[i]) and (u is None or minWeight[u] > minWeight[i]):
                u = i

        if parent[u] != u:
            selected.append((parent[u], u))

        res += minWeight[u] ** (1/2)
        added[u] = True

        # u에 인접한 간선 update
        for i in range(n):
            if (not added[i]) and (minWeight[i] > adj[u][i]):
                minWeight[i] = adj[u][i]
                parent[i] = u
    return res


def test():
    inputs = """2
3 1
0 0 1
0 1 2
0 1
10 5
-7 -7 10 -4 10 -4 -5 0 -10 -6
6 8 -5 3 -4 6 -10 4 -7 10
9 7
7 3
9 7
5 0
8 6"""
    inputs = inputs.split('\n')
    inputs.reverse()

    def parse():
        return list(map(int, inputs.pop().split()))

    t, = parse()
    for _ in range(t):
        n, m = parse()
        adj = [[None]*n for _ in range(n)]
        x = parse()
        y = parse()

        for i in range(n):
            adj[i][i] = 0
            for j in range(i, n):
                d = (x[i]-x[j])**2+(y[i]-y[j])**2
                adj[i][j] = d
                adj[j][i] = d

        for _ in range(m):
            a, b = parse()
            adj[a][b] = 0
            adj[b][a] = 0
        
        print(solve(adj))

test()

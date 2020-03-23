# 2020.3.21
# p959
# wrong

def solve(adj, delay):
    n = len(adj)

    dist = [[adj[i][j] for j in range(n)] for i in range(n)]

    order = [(b,a) for a,b in enumerate(delay)]
    order.sort()
    for _, k in order:
        for i in range(n):
            for j in range(n):
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][i])
                dist[i][j] = min(dist[i][j], adj[i][k]+adj[k][i]+delay[k])
    return dist

def test():
    inputs = """8 12
8 6 5 8 3 5 8 4
1 6 9
1 2 3
2 8 3
6 8 5
6 7 3
8 7 3
6 5 5
4 5 7
3 4 4
3 5 2
2 3 6
7 5 1
2
1 5
6 3"""
    inputs = inputs.split('\n')
    inputs.reverse()

    def parse():
        return list(map(int, inputs.pop().split()))
    v, e = parse()
    # 음주단속시간
    delay = parse()
    adj = [[float('inf')]*v for _ in range(v)] 
    print(adj)
    for _ in range(e):
        a, b, c = parse()
        adj[a-1][b-1] = c

    for i in range(v):
        adj[i][i] = 0

    dist = solve(adj, delay)

    t, = parse()
    for _ in range(t):
        start, end = parse()
        print(dist[start-1][end-1])

test()

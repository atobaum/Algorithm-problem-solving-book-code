# p930
# 2020.3.18
# not tested
from queue import PriorityQueue

def parseInt(str):
    return list(map(int, str.split()))

def ROUTING(adj):
    """
    adj[i] - List[(number, int)] - (dist, to)
    returns 0에서 n-1로 가는 최소 노이즈 
    """
    q = PriorityQueue()
    n = len(adj)
    dist = [1000] * n
    q.put((1, 0))
    while not q.empty():
        top = q.get()
        if dist[top[1]] < top[0]:
            continue
        for i in adj[top[1]]:
            nextDist = top[0] * i[0]
            if nextDist < dist[i[1]]:
                dist[i[1]] = nextDist
                q.put((nextDist, i[1]))
    return dist

def main():
    t, = parseInt(input())
    for _ in range(t):
        n, m = parseInt(input())
        adj = [[] for _ in range(n)]
        for _ in range(m):
            a, b, c = parseInt(input())
            adj[a].append((c, b))
            adj[b].append((c, a))
        print(ROUTING(adj))

def test():
    print(ROUTING(adj))
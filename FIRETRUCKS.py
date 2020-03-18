# p933
# 2020.3.18

from queue import PriorityQueue

def dijkstra(adj, start = 0):
    dist = [float('inf')] * (len(adj)+1)
    print(len(adj))
    q = PriorityQueue()
    q.put((0, start))

    while not q.empty():
        here = q.get()
        if dist[here[1]] < here[0]:
            continue

        for there in adj[here[1]]:
            nextDist = here[0] + there[0]
            if dist[there[1]] > nextDist:
                dist[there[1]] = nextDist
                q.put((nextDist, there[1]))
    return dist

def main():
    inputs = """8 12 3 2
1 2 3
1 6 9
2 3 6
3 4 4
3 5 2
4 5 7
6 5 5
8 6 5
6 7 3
8 7 3
7 5 1
2 8 3
2 3 5
4 6"""

    inputs = inputs.split('\n')
    inputs = [list(map(int, line.split())) for line in inputs]
    inputs.reverse()

    v, e, n, m = inputs.pop()
    adj = [[] for _ in range(v+1)] ## adj[v] is virtual node
    for _ in range(e):
        a, b, t = inputs.pop()
        adj[a-1].append((t, b-1))
        adj[b-1].append((t, a-1))
    fires = inputs.pop()
    firestations = inputs.pop()

    ## add edges to firestations from virtual node
    for fs in firestations:
        adj[v].append((0, fs-1))
    
    print(adj)
    dist = dijkstra(adj, v)
    print(dist)

    res = 0
    for fire in fires:
        res += dist[fire-1]
    
    print(res)
    # must be 16
 
main()
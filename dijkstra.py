# 2020.3.18

from queue import PriorityQueue

def Dijkstra(adj, start):
    """
    adj[i] - (a, b), whare a is the cost going i to b
    returns number[] which ith element is the shortest length from start to i
    """
    q = PriorityQueue()
    dist = [float('inf')] * len(adj)

    # (dist, node)
    q.put((0, start))

    while not q.empty():
        top = q.get()
        if dist[top[1]] < top[0]: continue
        for to in adj[top[1]]:
            nextDist = top[0] + to[0]
            if dist[to[1]] > nextDist:
                dist[to[1]] = nextDist
                q.put((nextDist, to[1]))
    return dist

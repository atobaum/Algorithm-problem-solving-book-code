# p946
# 2020.3.20

def bellmanFord(adj, start = 0):
    """
    adj[i] = [(cost, to)]
    """
    n = len(adj)
    dist = [float('inf')] * n
    dist[start] = 0

    for _ in range(n):
        updated = False
        for here in range(n):
            for (cost, to) in adj[here]:
                dCan = dist[here] + cost
                if dCan < dist[to]:
                    updated = True
                    dist[to] = dCan
        if not updated:
            break
    
    # check exsistence of minus cycle
    if updated:
        dist = []
    return dist

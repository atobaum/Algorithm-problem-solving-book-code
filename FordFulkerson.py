# 2020.3.23
# p.993

INF = float('inf')

def networkFlow(capacity, source = 0, sink = None):
    if sink is None:
        sink = len(source) - 1

    v = len(capacity)
    flow = [[0]*v for _ in range(v)]
    totalFlow = 0


    while True:
        parent = [None] * v
        q = []
        q.append(source)

        while len(q) != 0 and (parent[sink] is None):
            here = q.pop(0)
            for there in range(v):
                #print(here, there, capacity[here][there] - flow[here][there] )
                if ((capacity[here][there] - flow[here][there] > 0)
                    and (parent[there] is None)):
                    q.append(there)
                    parent[there] = here

        if parent[sink] is None:
            break
        
        amount = INF
        p = sink
        while True:
            if p == source:
                break
            amount = min(amount, capacity[parent[p]][p] - flow[parent[p]][p])
            p = parent[p]

        p = sink
        while True:
            if p == source:
                break
            flow[parent[p]][p] += amount
            flow[p][parent[p]] -= amount
            p = parent[p]

        totalFlow += amount

    return totalFlow

def test():
    capacity = [[0, 1000, 1000, 0], [0, 0, 1,0], [0, 0, 0, 1000], [0, 0, 0, 0]]
    print(networkFlow(capacity, 0, 3), " = 2000")

    capacity = [[0, 10], [0, 0]]
    print(networkFlow(capacity, 0, 1), " = 10")

# if __name__ == "__main__":
    # test()

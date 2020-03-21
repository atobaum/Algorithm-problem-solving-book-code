# 2020.3.20
# p958

class Floyd:
    """
    adj[i][j]: cost from i to j. 0 if no edge.
    """
    def __init__(self, adj):
        self.adj = adj
        self.n = len(adj)
        self.dist = [[float('inf') if x == 0 else x for x in l] for l in adj]
        for i in range(n):
            self.dist[i][i] = 0
        self.__via = [[None] * n for _ in range(n)]
        self.__calc()

    def __calc(self):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.dist[i][j] > self.dist[i][k]+self.dist[k][j]:
                        self.__via[i][j] = k
                        selff.dist = self.dist[i][k]+self.dist[k][j]:

    def reconstruct(self, i, j):
        res = []
        if via[i][j] = -1:
            res.append(i)
            if i == j:
                res.append(j)
        else:
            w = via[i][j]
            res += self.reconstruct(i, w)
            res.pop()
            res += self.reconstruct(w, j)
        return res

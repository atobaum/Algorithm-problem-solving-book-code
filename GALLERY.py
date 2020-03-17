# 2020.3.17
# p863

    
def GALLERY():
    # visited[i]: 1 for visited, 2 for cctv install
    # returns whether here is not watched(0) or watched(1) or cctv is installed at here(2)
    def solve(here, isroot):
        nonlocal adj, installed, visited
        ret = 0
        visited[here] = 1

        if isroot == True and len(adj[here]) == 0:
            ret = 2
            installed += 1

        for i in adj[here]:
            if visited[i] is not None:
                continue

            c = solve(i, False)
            if c == 0:
                installed += 1
                ret = 2
                break
            elif c == 2:
                ret = 1
        return ret

    c = int(input())
    for _ in range(c):
        g, h = list(map(int, input().split()))
        adj = [[] for _ in range(g)]
        for _ in range(h):
            a, b = list(map(int, input().split()))
            adj[a].append(b)
            adj[b].append(a)
        installed = 0
        visited = [None]*g
        for here in range(g):
            if visited[here] is None:
                solve(here, True)
        print(installed)
GALLERY()

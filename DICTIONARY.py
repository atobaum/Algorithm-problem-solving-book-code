# p831
# 2020.3.15
# uncompleted

from typings import List

def C2N(c):
    return ord(c) - ord('a')

def makeGraph(words: List[str]):
    adj = [[] for _ in range(26)]
    for i in range(len(words)-1):
        a = words[i]
        b = words[i+1]
        
        for j in range(len(a)):
            if a[j] != b[j]:
                adj[C2N(a[j])].append(C2N(b[j]))
                break;
    return adj

def topologicalSort(adj):
    visited = [None]*26
    order = []
    def dfs(here: int):
        visited[here] = 1
        for there in adj[here]:
            if visited[there] is not None:
                dfs(there)
                order.append(here)
    
    for i in range(26):
        if visited[i] is None:
            dfs(i)

    order.reverse()

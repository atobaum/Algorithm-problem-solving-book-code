#2020.3.15
# p842

from typing import List

def C2N(c):
    return ord(c) - ord('a')

def makeGraph(words: List[str]):
    # adj[i][j] - 알파벳 i에서 j로 가는 단어의 수
    adj = [[0]*26 for _ in range(26)]

    # graph[i][j]: List[str] - 알파벳 i시작, j로 끝나는 단어 목록
    graph = [[[] for _ in range(26)] for __ in range(26)]

    inbound = [0]*26
    outbound = [0]*26

    for w in words:
        s = C2N(w[0])
        e = C2N(w[len(w)-1])

        adj[s][e] += 1
        graph[s][e].append(w)
        inbound[e] += 1
        outbound[s] += 1

    return adj, graph, inbound, outbound

def getEulerCircuit(start: int, adj, circuit):
    for there in range(26):
        while adj[start][there] > 0:
            adj[start][there] -= 1
            getEulerCircuit(there, adj, circuit)
    circuit.append(start)
    return circuit

def getEulerCircuitOrTrail(adj, inbound, outbound):
    circuit = []
    for i in range(26):
        if outbound[i] - inbound[i] == 1:
            return getEulerCircuit(i, adj, circuit)
    
    for i in range(26):
        if outbound[i] > 0:
            return getEulerCircuit(i, adj, circuit)

    return []

def checkEuler(inbound, outbound):
    startCandidate = 0
    endCandidate = 0
    for i in range(26):
        d = outbound[i] - inbound[i]
        if d < -1 or d > 1:
            return false
        elif d == 1:
            startCandidate += 1
        elif d == -1:
            endCandidate += 1
    return startCandidate <= 1 and startCandidate == endCandidate

def solve(words):
    adj, graph, inbound, outbound = makeGraph(words)
    if not checkEuler(inbound, outbound):
        print("IMPOSSIBLE")
        return
    circuit = getEulerCircuitOrTrail(adj, inbound, outbound)
    circuit.reverse()
    
    if len(circuit) != len(words) + 1:
        print("IMPOSSIBLE")
        return

    res = ''
    for i in range(len(circuit) - 1):
        res +=graph[circuit[i]][circuit[i+1]].pop() + " "
    print(res)
    return

def WORDCHAIN():
    c = int(input())
    for _ in range(c):
        n = int(input())
        words = []
        for _ in range(n):
            words.append(input())
        solve(words)

if __name__ == '__main__':
    WORDCHAIN()

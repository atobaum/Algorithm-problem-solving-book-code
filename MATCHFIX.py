# 2020.3.23
# p1005
from utils import parse
from FordFulkerson import networkFlow

def test():
    inputs = """3
2 2
3 3
0 1
0 1
3 3
4 2 2
1 2
1 2
1 2
4 4
5 3 3 2
0 1
1 2
2 3
1 3"""
    inputs = parse(inputs)
    c, = inputs.pop()
    for _ in range(c):
        _, m = inputs.pop()
        win = inputs.pop()
        matches = []
        for _ in range(m):
            a, b = inputs.pop()
            matches.append((a, b))
        print(solve(win, matches))

def solve(win, matches):
    n = len(win)
    m = len(matches)
    V = 2 + n + m
    
    def canWinWith(totalWin):
        if max(win[1:]) > totalWin:
            return False

        # 0: start, 1: sink
        # 2+i: ith match
        # 2+m+i: ith member
        capacity = [[0]*V for _ in range(V)]
        for idx, match in enumerate(matches):
            capacity[0][2+idx] = 1
            capacity[2+idx][2+m+match[0]] = 1
            capacity[2+idx][2+m+match[1]] = 1

        for idx, w in enumerate(win):
            if idx == 0:
                capacity[2+m+idx][1] = totalWin - w
            else:
                capacity[2+m+idx][1] = totalWin - 1 - w

        res = networkFlow(capacity, 0, 1)
        return res == m

    totalWin = win[0]
    for _ in range(len(matches) + 1):
        if canWinWith(totalWin):
            return totalWin
        else:
            totalWin += 1
    return -1

test()

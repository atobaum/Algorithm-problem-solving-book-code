# 2020.3.17
# p861 SCC 구현

def SCC(adj):
    vertexCounter = 0
    sccCounter = 0
    n = len(adj)
    discovered = [None]*n
    sccId = [None]*n
    st = [] # stack

    # here을 루트로 하는 서브트리에서 역으로 갈 수 있는
    # 정점의 최소 발견 순서 return
    def solve(here):
        nonlocal vertexCounter,sccCounter, n, discovered, sccId, st 
        discovered[here] = vertexCounter
        ret = vertexCounter
        vertexCounter += 1

        st.append(here)
        for there in adj[here]:
            if discovered[there] is None: # 트리간선
                ret = min(ret, solve(there))
            # 교차간선, 역간선
            elif sccId[there] is None:
                ret = min(ret, discovered[there])

        # 잘라야할때
        if ret == discovered[here]:
            while True:
                top = st.pop()
                sccId[top] = sccCounter
                if top == here: break
            sccCounter += 1
        return ret
    
    for i in range(n):
        if discovered[i] is None:
            solve(i)
    return sccId

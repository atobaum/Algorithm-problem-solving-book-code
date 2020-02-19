# 접미사의 배열을 알파벳순으로 정렬한 배열
from functools import cmp_to_key

def getCompareFunc(group, t):
    # 오름차순 정렬.
    # 음수: 뒤의 것에 큼
    # 양수: 앞의 것이 큼
    def cmp(a, b):
        try:
            if group[a] != group[b]:
                return group[a] - group[b]
            return group[a+t] - group[b+t]
        except:
            print(a, b, t)
    return cmp

def suffixArray(str):
    n = len(str)

    # group[i]: S[i...] 가 속한 그룹 번호
    group = [ord(str[i]) for i in range(n)]
    group.append(-1)

    # 결과 배열.
    # ret[i]: i번째 접미사 배열.
    ret = [i for i in range(n)]

    # 접미사들의 t글자 기준으로 정렬.
    t = 1
    while t < n:
        cmpFunc = getCompareFunc(group, t)
        ret.sort(key = cmp_to_key(cmpFunc))
        t *= 2
        if t >= n: break

        newGroup = [-1 for i in range(n+1)]
        newGroup[ret[0]] = 0
        for i in range(1, n):
            # ret[i] > ret[i-1]일때
            if cmpFunc(ret[i], ret[i-1]) > 0:
                newGroup[ret[i]] = newGroup[ret[i-1]]+1
            else:
                newGroup[ret[i]] = newGroup[ret[i-1]]
        group = newGroup
    
    return ret

def indexToString(str, indices):
    return list(map(lambda i: str[i:], indices))

def suffixArrayString(str):
    return indexToString(str, suffixArray(str))

# print(suffixArrayString("mississipi"))
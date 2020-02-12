# 접두사도 되고 접미사도 되는 문자열의 길이들 출력
# 2020-02-13
# p 654

import KMP

def NAMING(str):
    pi = KMP.getPartialMatch(str)
    ret = []
    k = len(str)
    while k > 0:
        ret.append(k)
        k = pi[k-1]
    return ret

print(NAMING("ababbaba"))

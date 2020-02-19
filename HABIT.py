# p672
import SuffixArray

def commonPrefix(str, i, j):
    ret = 0
    while i < len(str) and j < len(str) and str[i] == str[j]:
        i += 1
        j += 1
        ret += 1
    return ret 
    
# str중 k번 이상 등장하는 문자열 중 가장 긴 부분 문자열의 길이 반환
def HABIT(str, k):
    a = SuffixArray.suffixArray(str)
    ret = 0
    for i in range(len(str) - k + 1):
        ret = max(ret, commonPrefix(str, a[i], a[i+k-1]))
    return ret

print(HABIT("uhmhellouhmmynameislibe", 2))
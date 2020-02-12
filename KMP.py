# O = n^2
def getPartialMatch1(str):
    ret = [0 for _ in range(len(str))]

    for begin in range(1, len(str)):
        for i in range(len(str)):
            if begin + i >= len(str):
                break
            if str[begin+i] != str[i]:
                break
            ret[begin+i] = max(ret[begin+i], i+1)
    return ret

# KMP 알고리즘 사용해서 구하기. O = n
def getPartialMatch(str):
    ret = [0 for _ in range(len(str))]
    begin = 1
    matched = 0
    while begin + matched < len(str):
        if str[begin+matched] == str[matched]:
            matched += 1
            ret[begin+matched-1] = matched
        else:
            #바로 틀림.
            if(matched == 0):
                begin += 1
            else:
                begin += matched - ret[matched - 1]
                matched = ret[matched - 1]
    return ret


def kmpSearch(str, searchStr):
    partialMatch = getPartialMatch(searchStr)
    ret = []

    begin = 0
    matched = 0
    while begin + matched < len(str):
        if (matched < len(searchStr)) and (str[begin+matched] == searchStr[matched]):
            matched += 1
            if matched == len(searchStr): ## 결과 찾음.
                ret.append(begin)
        else:
            #바로 틀림.
            if(matched == 0):
                begin += 1
            else:
                begin += matched - partialMatch[matched - 1]
                matched = partialMatch[matched - 1]
    return ret

print(kmpSearch("abcbadflk;jzxc;iovhnabcl;kasdjfabcacsvcsxczxcacabababc", "abc"))
print(getPartialMatch1("aabaabac"))
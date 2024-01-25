from collections import Counter

def solution(X, Y):
    xCounter = Counter(X)
    yCounter = Counter(Y)
    commonKey = sorted(set(xCounter.keys()) & set(yCounter.keys()))
    commonDict = {key: min(xCounter[key], yCounter[key]) for key in commonKey}
    if len(commonDict) == 1 and '0' in commonKey:
        return "0"
    answer = ''
    for key in sorted(commonDict.keys(), reverse=True):
        while commonDict[key] > 0:
            commonDict[key] -= 1
            answer += key
    if answer == "":
        return '-1'
    return answer
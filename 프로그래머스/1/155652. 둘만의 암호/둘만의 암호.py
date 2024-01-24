def solution(s, skip, index):
    answer = ''
    alphabet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    newAlpha = list(alphabet - set(skip))
    newAlpha.sort()
    
    for idx in range(len(s)):
        alphaIdx = newAlpha.index(s[idx]) + index
        newIdx = alphaIdx % len(newAlpha)
        answer+=newAlpha[newIdx]
    return answer

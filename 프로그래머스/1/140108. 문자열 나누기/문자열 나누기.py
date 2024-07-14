def solution(s):
    answer = 0
    notX = isX = 0
    for i in s:
        if notX == isX:
            answer += 1
            k = i
        if k ==i:
            isX += 1
        else:
            notX += 1
    return answer
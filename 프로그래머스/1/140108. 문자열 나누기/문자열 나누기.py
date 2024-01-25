def solution(s):
    answer = 0
    notX = isX = 0
    x = ""
    for alp in s:
        
        if not x:
            x = alp
            isX += 1
            continue
        if x == alp:
            isX += 1
        else:
            notX += 1
            
        if isX == notX:
            x = ""
            answer += 1
        print(x)
    if x != "":
        answer += 1
    return answer
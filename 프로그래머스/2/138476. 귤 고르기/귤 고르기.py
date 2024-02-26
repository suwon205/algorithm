def solution(k, tangerine):
    # 서로 다른 종류의 수를 최소화
    answer = cnt = 0
    tDict = {}
    for t in tangerine:
        if t in tDict:
            tDict[t] += 1
        else:
            tDict[t] = 1
    sorted_tDict = sorted(tDict.items(), key=lambda x: -x[1])
    idx = 0
    while True:
        if cnt >= k:
            break
        cnt += sorted_tDict[idx][1]
        idx += 1
        answer += 1
    return answer
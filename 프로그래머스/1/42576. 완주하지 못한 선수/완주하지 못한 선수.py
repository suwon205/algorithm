def solution(participant, completion):
    answer = ''
    #참여자 명단에만 있거나, 참여자 명단에서의 수가 많으면 된다.
    pDict = {} #참여자 딕셔너리
    cDict = {} #완주자 딕셔너리
    for pIdx in range(len(participant)):
        if participant[pIdx] not in pDict:
            pDict[participant[pIdx]] = 1
        else:
            pDict[participant[pIdx]] += 1
    
    for cIdx in range(len(completion)):
        if completion[cIdx] not in cDict:
            cDict[completion[cIdx]] = 1
        else:
            cDict[completion[cIdx]] += 1
    for p in pDict:
        if p not in cDict: #tc 1의 경우. 참여자에는 있으나 완주자에는 없는 경우
            return p
        else:
            if pDict[p] != cDict[p]:
                return p
    return answer
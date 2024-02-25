def solution(s):
    answer = []
    # 파싱
    elements = s[2:-2].split('},{')
    elements = [list(map(int, element.split(','))) for element in elements]
    # 파싱 완료
    elements.sort(key=len)
    newDict = dict()
    for idx in range(len(elements)):
        for id in elements[idx]:
            if id in newDict:
                newDict[id] += 1
            else:
                newDict[id] = 1

    for idx in newDict:
        answer.append(idx)
    return answer
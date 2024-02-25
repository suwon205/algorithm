def makeData(str):
    lst = []
    for i in range(0, len(str)-1):
        if str[i].isalpha() and str[i+1].isalpha():
            lst.append(str[i].lower()+str[i+1].lower())
    return lst

def countElement(lst):
    newDict = {}
    for i in lst:
        if i in newDict:
            newDict[i] += 1
        else:
            newDict[i] = 1
    return newDict

def jaccard(dicA, dicB, intersectionList, unionList):
    cntIntersection = 0
    cntUnion = 0
    print(dicA, dicB, intersectionList, unionList)
    for intersec in intersectionList:
        cntIntersection += min(dicA[intersec], dicB[intersec])
    for uni in unionList:
        if uni in dicA and uni in dicB:
            # 둘 다 있는 경우...
            cntUnion += max(dicA[uni], dicB[uni])
        elif uni in dicA:
            cntUnion += dicA[uni]
        else:
            cntUnion += dicB[uni]
    print(cntIntersection/cntUnion, '자카드', cntIntersection, cntUnion)
    return cntIntersection / cntUnion
    
    
    
def solution(str1, str2):
    answer = 0
    # J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
    listA = makeData(str1)
    dictA = countElement(listA)
    listB = makeData(str2)
    dictB = countElement(listB)
    unionList = set(listA).union(listB)
    intersectionList = set(listA).intersection(listB)
    if len(listA) == 0 and len(listB) == 0: #둘다 공집합인 경우
        answer = 1
    else:
        answer = jaccard(dictA, dictB, intersectionList, unionList)
    
    return int(answer * 65536)
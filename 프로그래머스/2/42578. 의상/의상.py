def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]] += 1
        else:
            dic[cloth[1]] = 1
    print(dic)
    for d in dic:
        answer *= (dic[d]+1)
        print(dic[d])
    return answer -1
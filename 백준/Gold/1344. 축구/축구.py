def percent(score, pct):
    cnt = 0
    while cnt != score: #점수를 낼 확률 구하기
        pct *= occur
        cnt += 1
    for i in range(18-score):
        pct *= notoccur
    return pct

def par(k):
    global dic
    if k == 18:
        if sum(res) not in PN: #소수가 아닌 경우
            dic[sum(res)] += 1
    else:
        res[k] = 0
        par(k+1)
        res[k] = 1
        par(k+1)

# A = int(input())/100
# notA = 1 - A
# B = int(input())/100
# notB = 1 - B
# 최대 18점 득점 가능(5분당 1골, 90분 플레이)
# 0~16에서의 소수는 2, 3, 5, 7, 11, 13, 17
# 0~16에서의 소수가 아닌 수는 0,1,4,6,8,9,10,12,14,15,16,18
# 적어도 한 팀이 소수로 득점할 확률 = 1 - 두 팀이 소수로 득점하지 않을 확률
PN = [2, 3, 5, 7, 11, 13, 17]
percent_list = [0]*2
for a in range(2):
    dic = {0: 0, 1: 0, 4: 0, 6: 0, 8: 0, 9: 0, 10: 0, 12: 0, 14: 0, 15: 0, 16: 0, 18: 0}  # 경우의 수를 전부 정리

    occur = int(input())/100
    notoccur = 1 - occur
    res = [0] * 18
    par(0)
# print(dic)
    for i in dic:
        dic[i] = percent(i,1) * dic[i] # 경우의 수 * 확률. 소수가 아닌 득점을 할 확률.
    percent_list[a] = sum(dic.values())
    # print(dic)
    # print(percent_list)
# if percent_list[0] == 1:
print(1-percent_list[0]*percent_list[1])
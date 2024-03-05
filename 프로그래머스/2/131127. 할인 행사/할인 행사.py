def solution(want, number, discount):
    # 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입
    answer = 0
    # dic = dict()
    # for idx in range(len(discount)):
    #     if discount[idx] in dic:
    #         dic[discount[idx]].append(idx)
    #     else:
    #         if discount[idx] in want:
    #             dic[discount[idx]] = [idx]
    # if len(want) != len(dic):
    #     return 0
    for day in range(len(discount) - 9):
        flag = True
        lst = discount[day : day + 10]
        temp = []
        for idx in range(len(want)):
            # print(want[idx], lst.count(want[idx]), number[idx])
            if lst.count(want[idx]) == 0 or lst.count(want[idx]) != number[idx]:
                flag = False
                break
        #     print(want[idx], lst.count(want[idx]), number[idx], "여기 옴", day)
        # print('여긴 옴?', day)
        if flag:
            answer +=1
            
    return answer
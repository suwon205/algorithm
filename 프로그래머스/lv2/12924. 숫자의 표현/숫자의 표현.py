def solution(n):
    answer = 0
    lst = []
    for num in range(n+1):
        lst.append(num)
    print(lst)
    for st in range(1, n):
        for ed in range(st+1, n+1):
            # print(st, ed, lst[st:ed], sum(lst[st:ed]))
            if sum(lst[st:ed]) == n:
                # st = ed + 1
                answer += 1
                print(st, ed, lst[st:ed])
            if sum(lst[st:ed]) > n:
                break
    return answer + 1
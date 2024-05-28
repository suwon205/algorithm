def solution(n, lost, reserve):
    answer = 0
    r_lost = list(set(lost) - set(reserve))
    r_reserve = list(set(reserve) - set(lost))
    lst = [1 for _ in range(n)]
    for idx in r_lost:
        lst[idx - 1] -= 1
    for idx in r_reserve:
        lst[idx - 1] += 1
    for idx in range(n):
        if lst[idx] == 0:
            if idx > 0 and lst[idx - 1] == 2:
                lst[idx - 1] -= 1
                lst[idx] += 1
            elif idx < n - 1 and lst[idx + 1] == 2:
                lst[idx + 1] -= 1
                lst[idx] += 1
    print(lst)
    for l in lst:
        if l > 0:
            answer += 1
    return answer
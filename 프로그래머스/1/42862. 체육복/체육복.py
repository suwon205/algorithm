def solution(n, lost, reserve):
    answer = 0
    students = [1] * n
    
    lost_set = list(set(lost) - set(reserve)) # 진짜로 잃어버린 경우만 남도록
    reserve_set = list(set(reserve) - set(lost)) # 진짜로 여분이 있는 경우만 남도록
    
    for idx in lost_set:
        students[idx - 1] -= 1
    for idx in reserve_set:
        students[idx - 1] += 1
    
    for idx in range(n):
        if students[idx] == 0:
            if idx > 0 and students[idx - 1] >= 2:
                students[idx] += 1
                students[idx - 1] -= 1
            elif idx < n - 1 and students[idx + 1] >= 2:
                students[idx] += 1
                students[idx + 1] -= 1

    for cloth in students:
        if cloth:
            answer += 1
    return answer
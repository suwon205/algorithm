from collections import deque

def solution(priorities, location):
    answer = 0
    lst = deque()
    for idx in range(len(priorities)):
        lst.append([idx, priorities[idx]])
    while lst:
        maxP = max(lst, key = lambda x : x[1])[1]
        job = lst.popleft()
        if maxP == job[1]: # 현재 작업이 가장 높은 우선 순위를 가진 경우
            answer += 1
            if job[0] == location:  # 원하는 작업이 완료된 경우
                break
        else:
            lst.append(job)
    return answer
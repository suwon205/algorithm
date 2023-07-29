from collections import deque

def solution(queue1, queue2):
    answer = -1
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sumQ1 = sum(queue1)
    sumQ2 = sum(queue2)
    cnt = 0
    if (sumQ1 + sumQ2) %2 == 1:
        return answer
    
    while True:
        if cnt == len(queue1) * 4:
            return answer
        if sumQ1 > sumQ2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sumQ1 -= tmp
            sumQ2 += tmp
        elif sumQ1 < sumQ2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sumQ1 += tmp
            sumQ2 -= tmp
        elif sumQ1 == sumQ2:
            return cnt
        cnt += 1
    return answer
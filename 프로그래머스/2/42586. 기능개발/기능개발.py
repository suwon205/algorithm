from collections import deque

def solution(progresses, speeds):
     # 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있음
     # 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포
    answer = []
    leftP = deque()
    day = 0
    for idx in range(len(progresses)):
        if (100 - progresses[idx]) % speeds[idx] != 0:
            leftP.append((100 - progresses[idx]) // speeds[idx] + 1)
        else:
            leftP.append((100 - progresses[idx]) // speeds[idx])
    print(leftP)
    idx = 0
    temp = 0
    flag = False
    while leftP:
        if leftP[idx] <= day:
            # 배포 가능
            temp += 1
            # print('배포 가능한 day', day, temp, leftP)
            leftP.popleft()
            # answer.append(temp)
            flag = True
        else:
            # 배포 불가능
            if flag:
                answer.append(temp)
            temp = 0
            day += 1
            flag = False
        # print(leftP, day, temp)
        if not leftP:
            answer.append(temp)
    return answer
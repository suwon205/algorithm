from collections import deque

def solution(arr):
    answer = []
    arr = deque(arr)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    while arr:
        temp = arr.popleft()
        if answer and answer[-1] == temp:
            continue
        answer.append(temp)
    return answer
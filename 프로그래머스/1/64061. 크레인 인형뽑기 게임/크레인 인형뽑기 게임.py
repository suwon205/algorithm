def solution(board, moves):
    answer = 0
    stack = [0] * len(moves) # 뽑은 인형을 저장해둘 것
    lastIdx = 0 # 인형을 더해줄 인덱스
    new_array = [list(row) for row in zip(*board)]
    for move in moves:
        for idx in range(len(board)):
            if new_array[move-1][idx] != 0: #옮길 인형
                if lastIdx and stack[lastIdx-1] == new_array[move-1][idx]: # 스택 마지막 인형이 내가 넣어줄 인형과 같은 경우
                    stack[lastIdx-1] = 0
                    lastIdx -= 1
                    answer += 2
                else: # 새 인형을 더해주는 경우
                    stack[lastIdx] = new_array[move-1][idx]
                    lastIdx += 1
                new_array[move-1][idx] = 0 # 현재 array에서 뽑은 인형을 무조건 없애주기
                break
    return answer
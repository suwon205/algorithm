def solution(numbers):
    stack = []  # 큰 수를 찾지 못한 숫자들을 저장할 스택
    answer = [-1] * len(numbers)  # 초기값을 -1로 설정한 결과 리스트

    for idx, num in enumerate(numbers):
        # 스택이 비어있지 않고 현재 숫자가 스택의 맨 위에 있는 숫자보다 크다면
        # 해당 숫자가 더 큰 수이므로 answer에 해당 숫자를 저장하고 스택에서 제거
        while stack and num > numbers[stack[-1]]:
            answer[stack.pop()] = num
        # 현재 숫자의 인덱스를 스택에 저장
        stack.append(idx)

    return answer

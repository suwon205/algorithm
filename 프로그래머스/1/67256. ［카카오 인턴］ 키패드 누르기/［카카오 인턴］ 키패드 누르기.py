def solution(numbers, hand):
    answer = ''
    keypad = {
        1 : [0, 0], 2 : [0, 1], 3 : [0, 2],
        4 : [1, 0], 5 : [1, 1], 6 : [1, 2],
        7 : [2, 0], 8 : [2, 1], 9: [2, 2],
        '*' : [3, 0], 0 : [3, 1], '#' : [3, 2]
    }
    # 초반 손의 위치 설정
    leftPos = keypad['*']
    rightPos = keypad['#']
    
    leftKey = [1, 4, 7]
    rightKey = [3, 6, 9]
    for idx in range(len(numbers)):
        if numbers[idx] in leftKey:
            answer += 'L'
            leftPos = keypad[numbers[idx]]
        elif numbers[idx] in rightKey:
            answer += 'R'
            rightPos = keypad[numbers[idx]]
        else:
            rightDis = abs(rightPos[0] - keypad[numbers[idx]][0]) + abs(rightPos[1] - keypad[numbers[idx]][1])
            leftDis = abs(leftPos[0] - keypad[numbers[idx]][0]) + abs(leftPos[1] - keypad[numbers[idx]][1])
            if rightDis > leftDis:
                answer += 'L'
                leftPos = keypad[numbers[idx]]
            elif rightDis < leftDis:
                answer += 'R'
                rightPos = keypad[numbers[idx]]
            else: # 양손에서부터의 길이가 같은 경우
                if hand == 'right':
                    answer += 'R'
                    rightPos = keypad[numbers[idx]]
                else:
                    answer += 'L'
                    leftPos = keypad[numbers[idx]]
    return answer
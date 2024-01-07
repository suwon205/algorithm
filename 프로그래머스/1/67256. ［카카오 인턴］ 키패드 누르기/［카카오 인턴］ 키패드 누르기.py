def solution(numbers, hand):
    answer = ''
    
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
       4: [1, 0], 5: [1, 1], 6: [1, 2],
       7: [2, 0], 8: [2, 1], 9: [2, 2],
       '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    leftPos = dic['*']
    rightPos = dic['#']
    
    for number in numbers:
        curPos = dic[number]
        
        if number == 1 or number == 4 or number == 7:
            answer += "L"
            leftPos = curPos
        elif number == 3 or number == 6 or number == 9:
            answer += "R"
            rightPos = curPos
        else:
            leftDistance = 0
            rightDistance = 0
            
            for a, b, c in zip(leftPos, rightPos, curPos):
                leftDistance += abs(a-c)
                rightDistance += abs(b-c)
            
            if leftDistance < rightDistance:
                answer += "L"
                leftPos = curPos
                
            elif leftDistance > rightDistance:
                answer += "R"
                rightPos = curPos
            else:
                if hand == "right":
                    answer += "R"
                    rightPos = curPos
                else:
                    answer += "L"
                    leftPos = curPos
    return answer

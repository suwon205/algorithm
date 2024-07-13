def solution(s):
    pCount = yCount = 0
    for c in s:
        if c == 'p' or c == 'P':
            pCount +=1
        elif c == 'y' or c == 'Y':
            yCount += 1
    if pCount == yCount:
        return True
    print('Hello Python')

    return False
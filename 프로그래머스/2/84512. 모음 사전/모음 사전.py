def solution(word):
    answer = 0
    words = ['A', 'E','I', 'O', 'U']
    tempArr = []
    def rec(depth, curWord):
        if depth <= 5:
            tempArr.append(curWord)
            for i in range(5):        
                rec(depth + 1, curWord + words[i])
    rec(0, '')
    # print(tempArr)
    return tempArr.index(word)
    # return answer
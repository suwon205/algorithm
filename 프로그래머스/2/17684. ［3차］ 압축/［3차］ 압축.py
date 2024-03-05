def solution(msg):
    answer = []
    alphabet_dict = {}
    for index in range(1, 27):
        letter = chr(index + 64)
        alphabet_dict[letter] = index
    firstIdx = 0
    lastIdx = 1
    lastVal = 27
    while lastIdx <= len(msg):
        curWord = msg[firstIdx : lastIdx]
        newWord = msg[firstIdx : lastIdx + 1]
        if newWord in alphabet_dict:
            lastIdx += 1
        else:
            answer.append(alphabet_dict[curWord])
            alphabet_dict[newWord] = lastVal
            lastVal += 1
            firstIdx = lastIdx
            lastIdx += 1
    answer.append(alphabet_dict[msg[firstIdx:lastIdx]])
    
    # while msg:
    #     if msg[firstIdx : lastIdx] in alphabet_dict: #있는 경우
    #         answer.append(alphabet_dict[msg[firstIdx : lastIdx]])
    #         msg = msg[lastIdx:]
    #     print(answer, msg[firstIdx : lastIdx])
        # if msg[firstIdx : lastIdx+2] in alphabet_dict: #알파벳에 있는 경우
        #     answer.append(msg[firstIdx:lastIdx])
        # else:
        #     alphabet_dict[firstIdx:lastIdx] = lastVal
        #     lastVal += 1
        # lastIdx += 1
        # print(alphabet_dict)
    return answer
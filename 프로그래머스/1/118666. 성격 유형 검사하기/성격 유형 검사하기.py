def solution(survey, choices):

    score = {'R':0, 'T':0, 'C':0, 'F':0, 'M':0, 'J':0, 'A':0, 'N':0}
    ans_first = {1:3, 2:2, 3:1}
    ans_second = {5:1, 6:2, 7:3}
    answer = ''

    for idx in range(len(survey)):
        if choices[idx] in ans_first: #앞선 선지 스코어 올려줄 경우
            score[survey[idx][0]] += ans_first[choices[idx]]
        elif choices[idx] in ans_second:
            score[survey[idx][1]] += ans_second[choices[idx]]

    if score['R'] < score['T']:
        answer += 'T'
    else:
        answer += 'R'
    if score['F'] > score['C']:
        answer += 'F'
    else:
        answer += 'C'
    if score['M'] > score['J']:
        answer += 'M'
    else:
        answer += 'J'
    if score['N'] > score['A']:
        answer += 'N'
    else:
        answer += 'A'

    return answer
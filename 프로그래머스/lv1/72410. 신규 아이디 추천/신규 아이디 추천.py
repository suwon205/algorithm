def solution(new_id):
    answer = ''
    #st1
    new_id = new_id.lower()
    #st2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    #st3
    while '..' in answer:
        answer = answer.replace('..', '.')
    #st4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    #st5
    if answer == '':
        answer = 'a'
    #st6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    #st7
    while len(answer) < 3:
        answer += answer[-1]
    return answer


# print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."	))
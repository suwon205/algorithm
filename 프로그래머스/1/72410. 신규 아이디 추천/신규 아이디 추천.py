def rule2and3(str):
    tempS = ''
    for c in str:
        if c.isalpha() or c.isdigit() or c == '-' or c == '_':
            tempS += c
        if c == '.':
            if tempS != '' and tempS[-1] != '.':
                tempS += c
            elif tempS == '':
                tempS += c
    return tempS

def r4(str):
    while True:
        if str and str[0] == '.':
            str = str[1:]
        if str and str[-1] == '.':
            str = str[:-1]
        break
    return str

def solution(new_id):
    answer = ''
    new_id = new_id.lower() # 규칙 1
    new_id = rule2and3(new_id) # 규칙 2,3
    new_id = r4(new_id) # 규칙 4
    if not new_id:
        new_id = 'a' # 규칙 5
    if len(new_id) >= 16:
        print(new_id)
        new_id = new_id[:15] # 규칙 6
        print('R6', new_id)
        if new_id[-1] == '.':
            new_id = new_id[:14]
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id = new_id + new_id[-1]
    print(new_id)
    return new_id
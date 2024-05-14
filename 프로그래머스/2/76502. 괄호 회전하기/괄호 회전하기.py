def solution(s):
    answer = 0
    stack = []
    dict = {'(' : 0, ')':0, '[' : 0, ']' : 0, '{' : 0, '}' : 0}
    for char in s:
        dict[char] += 1
    if dict['('] != dict[')'] or dict['{'] != dict['}'] or dict['['] != dict[']']:
        #애초에 닫는 괄호, 여는 괄호의 수가 다르다면 result 올릴 수 없다
        return 0
    for i in range(len(s)):
        flag = False
        newS = s[i:] + s[:i]
        for char in newS:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
                flag = True
            else:
                if not stack:
                    flag = False
                    break
                else:
                    if char == ')' and stack[-1] == '(':
                        stack.pop()
                    elif char == '}' and stack[-1] == '{':
                        stack.pop()
                    elif char == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        break
        if flag and not stack:
            answer += 1

    return answer
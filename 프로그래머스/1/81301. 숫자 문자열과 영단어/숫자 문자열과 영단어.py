dic = {'zero' : '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def solution(s):
    answer = ''
    idx = 0
    while idx < len(s):
        if s[idx].isdigit():
            answer += s[idx]
            idx += 1
        else:
            for end in range(idx + 1, len(s) + 1):
                tmp = s[idx:end]
                if tmp in dic:
                    answer += dic[tmp]
                    idx = end
                    break
    return int(answer)

result = solution('23four5six7')
print(result)

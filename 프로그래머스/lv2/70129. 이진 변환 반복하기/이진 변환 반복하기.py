def solution(s):
    answer = []
    cnt = 0
    step = 0
    while s != '1':
        tmp = ''
        # 0 제거
        for char in s:
            if char != '0':
                tmp += char
            else: cnt += 1
        # 길이만큼 이진 변환
        l = len(tmp)
        s = bin(l)
        s = s[2:]
        step += 1
    answer.append(step)
    answer.append(cnt)
    return answer
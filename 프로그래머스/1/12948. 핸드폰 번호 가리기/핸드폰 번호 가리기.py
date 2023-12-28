def solution(phone_number):
    answer = ''
    l = len(phone_number)
    for idx in range(l-4):
        answer += '*'
    for idx in range(l-4,l):
        answer += phone_number[idx]
    return answer
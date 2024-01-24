def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for idx in range(len(participant)):
        if idx == len(participant) -1 or participant[idx] != completion[idx]:
            return participant[idx]
    return answer
def solution(N, stages):
    answer = []
    # 스테이지에 도달했으나 아직 클리어하지 못한 경우
    challenge = {}
    # 스테이지에 도달한 경우
    success = {}
    percent = [] # 실패율
    
    for i in range(1, N + 2):
        challenge[i] = 0
        
    for stage in stages:
        for i in range(1, stage + 1):
            challenge[i] += 1
    print(challenge)
    for i in range(1, len(challenge)):
        success[i] = challenge[i] - challenge[i + 1]
    print(success)
    
    for i in range(1, N + 1):
        if challenge[i] == 0:
            percent.append((0, i))
        else:
            percent.append((int(success[i]) / int(challenge[i]), i))
    print(percent)
    percent.sort(key = lambda x: -x[0])
    for p in percent:
        answer.append(p[1])
    return answer
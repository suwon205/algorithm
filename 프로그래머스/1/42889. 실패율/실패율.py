def solution(N, stages):
    answer = []
    challenge = [0]*(N+1) # challenge[n]은 n스테이지에 도전한 사람의 수
    fail = [0]*(N+1) # 성공한 사람의 수
    percent = []
    for stage in stages:
        for i in range(stage):
            challenge[i] += 1
    for idx in range(N):
        fail[idx] = challenge[idx] - challenge[idx+1]
    print(challenge, fail)
    for idx in range(N):
        if challenge[idx] == 0:
            percent.append([idx+1, 0])
        else:
            percent.append([idx+1, fail[idx]/challenge[idx]])
    print(percent)
    percent.sort(key = lambda x : (-x[1], x[0]))
    print(percent)
    for p in percent:
        answer.append(p[0])
    return answer
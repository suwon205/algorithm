def solution(N, stages):
    challenge = {} # 스테이지에 도달한 플레이어 수
    success = {} # 성공한 사람 수 기재해주자
    percent = [] # 실패율 기록하기
    for i in range(1,N+2):
        challenge[i] = 0
    print(challenge)
    for stage in stages:
        for i in range(1, stage + 1):
            challenge[i] += 1
    for idx in range(1, len(challenge)):
        success[idx] = challenge[idx] - challenge[idx+1]
    for idx in range(1, N + 1):
        if challenge[idx] == 0:
            percent.append((0, idx))
        else:
            percent.append((int(success[idx]) / int(challenge[idx]), idx))
    percent.sort(key=lambda x: -x[0])  # 내림차순, 오름차순 정렬
    answer = []
    for p in percent:
        answer.append(p[1])
    return answer
def solution(N, stages):
    answer = []
    # stages = 도전중인 스테이지를 나타냄
    successStages = [0] * (N+1)
    failStages = [0] * (N+1)
    failPercent = [0] * N
    for stage in stages:
        for idx in range(stage):
            successStages[idx] += 1
    for idx in range(N):
        failStages[idx] = successStages[idx] -successStages[idx+1]
    for idx in range(N):
        if successStages[idx] == 0:
            failPercent[idx] = (idx+1,0)
        else:
            failPercent[idx] = (idx + 1, failStages[idx]/successStages[idx])
    failPercent.sort(key = lambda x : (-x[1], x[0]))
    for idx in range(N):
        answer.append(failPercent[idx][0])
    return answer
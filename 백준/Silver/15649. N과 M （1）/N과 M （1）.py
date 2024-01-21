N,M= map(int,input().split())
# 1부터 N까지의 자연수 모임 중 길이가 M인 수열 뽑기
result = []
visit = [False] * (N+1)

def partial(k):
    if k==M:
        print(' '.join(map(str,result)))
        return
    for i in range(1,N+1):
        if not visit[i]:
            visit[i] = True
            result.append(i)
            partial(k+1)
            visit[i] = False #추후 영향을 주지 않기 위해 원복시킨다.
            result.pop() #추후 영향을~ 원복 2

partial(0)
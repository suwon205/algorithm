N,M = map(int, input().split())
res = []
#이 문제의 포인트는 같은 수를 출력해도 골라도 된다는 것! 1~3의 수 중 2개의 수를 고를 때 2,2의 출력이 가능함!
def dfs(k):
    if k==M: #다 돈 경우
        print(' '.join(map(str,res)))
        return

    else:
        for i in range(1,N+1):
            res.append(i)
            dfs(k+1)
            res.pop()

dfs(0)
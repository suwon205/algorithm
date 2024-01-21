def backtracking(st):
    if st == M:
        for i in res:
            print(i, end=' ')
        print()
    else:
        for idx in range(N):
            if not used[idx]:
                res[st] = lst[idx]
                used[idx] = True
                backtracking(st + 1)
                used[idx] = False

N, M = map(int, input().split())
lst = list(map(int,input().split()))
lst.sort()
res = [0] * M
used = [False] * (N+1)
backtracking(0)
def backtracking():
    if len(res) == M:
        for i in res:
            print(i, end=' ')
        print()
    else:
        for i in range(N):
            res.append(lst[i])
            backtracking()
            res.pop()

N,M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
res = []
backtracking()
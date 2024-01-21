def backtracking(st):
    if len(res) == M:
        for i in res:
            print(i, end=' ')
        print()
        # print(res)
    else:
        for i in range(st, N):
            res.append(lst[i])
            backtracking(i)
            res.pop()

N,M =map(int, input().split())
res = []
lst = list(map(int, input().split()))
lst.sort()
backtracking(0)
def backtracking(st):
    if len(lst) == M:
        print(' '.join(map(str, lst)))
        return
    else:
        for i in range(st, N + 1):
            if not used[i]:
                lst.append(i)
                backtracking(i)
                lst.pop()

N,M = map(int, input().split())
used = [False] * (N+1)
lst = []
backtracking(1)
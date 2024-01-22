def backtracking():
    if len(res) == M:
        ans.add(tuple(res))
    else:
        for i in range(N):
            if not used[i]:
                used[i] = True
                res.append(lst[i])
                backtracking()
                used[i] = False
                res.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
res = []
ans = set()
used = [False] * N
backtracking()
answer = list(ans)
answer.sort()
for idx in range(len(answer)):
    for num in answer[idx]:
        print(num, end=' ')
    print()

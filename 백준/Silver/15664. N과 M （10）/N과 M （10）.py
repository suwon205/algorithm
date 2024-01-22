def backtracking(st):
    if len(res) == M:
        ans_set.add(tuple(res))
    else:
        for i in range(st, N):
            if not used[i]:
                res.append(lst[i])
                used[i] = True
                backtracking(i+1)
                used[i] = False
                res.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

res = []
ans_set = set()
used = [False] * N

backtracking(0)
answer = list(ans_set)
answer.sort()

for i in range(len(answer)):
    for num in answer[i]:
        print(num, end=' ')
    print()
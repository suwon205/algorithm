def recursion(st):
    if len(res) == M:
        ans.add(tuple(res))
    else:
        for i in range(st, N):
            res.append(lst[i])
            recursion(i)
            res.pop()

N,M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

res = []
ans = set()

recursion(0)
answer = list(ans)
answer.sort()

for i in range(len(answer)):
    for num in answer[i]:
        print(num, end=' ')
    print()

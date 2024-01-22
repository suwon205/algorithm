def rec():
    if len(res) == M:
        ans.add(tuple(res))
    else:
        for i in range(N):
            res.append(lst[i])
            rec()
            res.pop()

N,M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

res = []
ans = set()
rec()

answer = list(ans)
answer.sort()

for i in range(len(answer)):
    for num in answer[i]:
        print(num, end= ' ')
    print()
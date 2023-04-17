N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
lst.sort(key=lambda x : (x[1], x[0]))
tmp = [lst[0]]
for i in range(1,N):
    if tmp[-1][1] <= lst[i][0]:
        tmp.append(lst[i])
print(len(tmp))
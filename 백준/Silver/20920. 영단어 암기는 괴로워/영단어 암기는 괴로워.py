N,M = map(int, input().split())
worddic = {}
for _ in range(N):
    tmp = input()
    if len(tmp) >= M:
        if tmp not in worddic:
            worddic[tmp] = 1
        else:
            worddic[tmp] += 1
maxF = max(worddic.values())
note = [[] for _ in range(maxF)]
for i in worddic:
    note[maxF-worddic[i]].append(i)
for page in note:
    sort_page = sorted(page, key=lambda x:(-len(x), x))
    for i in sort_page:
        print(i)
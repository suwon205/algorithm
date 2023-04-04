N,L = map(int, input().split())
pond = []
for _ in range(N):
    s,e = map(int, input().split())
    pond.append((s,e))
pond.sort(key=lambda x : x[1])
cnt = 0
pannelIdx = 0
for s,e in pond:
    if pannelIdx > e:
        continue
    elif pannelIdx > s:
        s = pannelIdx
    while s<e:
        cnt += 1
        s += L
    pannelIdx = s
print(cnt)
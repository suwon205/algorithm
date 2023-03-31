import sys


N,L = map(int, input().split())
len_check = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

len_sort = sorted(len_check, key= lambda x : x[1])
cnt = 0
pannelIdx = 0

for s,e in len_sort:
    if pannelIdx>e: #볼 필요 없는 경우
        continue
    elif pannelIdx>s: #조금이라도 판넬의 끝이 웅덩이의 시작을 커버하고 있으면...
        s = pannelIdx
    while s<e:
        cnt += 1
        s += L
    pannelIdx = s
print(cnt)
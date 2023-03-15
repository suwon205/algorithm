import sys
input = sys.stdin.readline
from itertools import combinations

N,M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
home_list =[] #집이 저장될 리스트
chicken = [] #가게가 저장될 리스트
res = 999999
#치킨집과의 거리가 가장 가까운 치킨집 N개만 남기기
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            home_list.append((r,c))
        elif arr[r][c] == 2:
            chicken.append((r,c))

for temp in combinations(chicken, M): #치킨집 리스트에서 M개를 고른 조합 돌기. 변수 temp
    tmp_answer = 0
    for home in home_list:
        ln = 999999999
        for k in range(M):
            ln = min(ln, abs(home[0]-temp[k][0]) + abs(home[1] - temp[k][1])) #x좌표 gap + y 좌표 gap과 ln의 비교!
        tmp_answer += ln
    res = min(tmp_answer, res)
print(res)
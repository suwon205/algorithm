T = int(input())

for tc in range(1,T+1):
    N,M = map(int, input().split())

    ls = [list(map(int, input().split())) for _ in range(N)]
    maxV =0
    for r in range(N):
        for c in range(M):
            tmpsum = ls[r][c]
            for k in [(1,0),(-1,0),(0,-1),(0,1)]:
                nr = r + k[0]
                nc = c + k[1]
                if 0<=nr<N and 0<=nc<M:
                    tmpsum += ls[nr][nc]
            if maxV < tmpsum:
                maxV = tmpsum
    print(f'#{tc} {maxV}')
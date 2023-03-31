def par(k, score, cal):
    global ans
    if cal > L: #백 트래킹
        return
    if k == N:
        if cal <= L:
            ans.append(score)
    else:
        par(k+1, score+inform[k][0], cal + inform[k][1]) #k번째 재료가 들어가는 경우
        par(k+1, score, cal) #k번째 재료가 들어가지 않는 경우


T = int(input())
for tc in range(1,T+1):
    N,L = map(int, input().split()) #재료의 수 N, 제한 칼로리 L
    inform = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    par(0,0,0)
    print(f'#{tc} {max(ans)}')

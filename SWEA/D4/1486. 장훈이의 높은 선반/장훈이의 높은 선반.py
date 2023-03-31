def par(k, Top_Height):
    global minV
    if Top_Height < B:  # 백 트래킹
        return
    if k == N:
        if minV > Top_Height:
            minV = Top_Height
            return minV
    else:
        par(k + 1, Top_Height - lst[k])
        par(k + 1, Top_Height)


T = int(input())
for tc in range(1, T + 1):
    minV = 99999999999999
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    par(0, sum(lst))
    print(f'#{tc} {minV-B}')
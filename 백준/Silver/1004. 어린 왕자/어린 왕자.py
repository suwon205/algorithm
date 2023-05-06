T = int(input())
for tc in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    cnt = 0

    for _ in range(N):
        x,y,r = map(int, input().split())
        gap1 = (x1-x)**2 + (y1-y)**2
        gap2 = (x2-x)**2 + (y2-y)**2

        if gap1 < r**2 and gap2 < r**2:
            continue
        elif gap1 < r**2 or gap2< r**2:
            cnt += 1
    print(cnt)
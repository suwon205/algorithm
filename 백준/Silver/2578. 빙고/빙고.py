c = [list(map(int, input().split())) for _ in range(5)]
speak = []
for _ in range(5):
    speak += list(map(int, input().split()))


def check():
    bingo = 0

    # 가로
    for x in c:
        if x.count(0) == 5:
            bingo += 1
    # 세로
    for i in range(5):
        y = 0
        for j in range(5):
            if c[j][i] == 0:
                y += 1
        if y == 5:
            bingo += 1

    # 왼쪽위 대각선
    d1 = 0
    for i in range(5):
        if c[i][i] == 0:
            d1 += 1

    if d1 == 5:
        bingo += 1

    # 오른쪽위 대각선
    d2 = 0
    for i in range(5):
        if c[i][4 - i] == 0:
            d2 += 1

    if d2 == 5:
        bingo += 1

    return bingo

cnt = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if speak[i] == c[x][y]:
                c[x][y] = 0
                cnt += 1

    if cnt >= 12: #12가 넘어가면서부터 빙고가 가능함
        result = check()

        if result >= 3:
            print(i + 1)
            break
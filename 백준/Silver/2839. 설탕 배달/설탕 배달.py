N = int(input())

sugar_5 = N // 5
sugar_3 = 0
N %= 5

while sugar_5 >= 0:
    if N % 3 == 0:
        sugar_3 = (N // 3)
        N -= 3 * sugar_3
        break

    sugar_5 -= 1
    N += 5

if N != 0:
    print(-1)
else:
    print(sugar_5 + sugar_3)
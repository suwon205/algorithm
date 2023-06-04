W, M, intern = map(int, input().split())
cnt = 0
while W >= 2 and M >= 1 and W+M-3>=intern:
    cnt += 1
    W -= 2
    M -= 1
print(cnt)
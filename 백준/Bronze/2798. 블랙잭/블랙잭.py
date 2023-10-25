N, M = map(int, input().split(' '))
card = list(map(int, input().split(' ')))

sumMax = 0
for i in range(N-2):
    for k in range(i+1, N-1):
        for j in range(k+1, N):
            if sum([card[i], card[k], card[j]]) > sumMax and sum([card[i], card[k], card[j]]) <= M:
                sumMax = sum([card[i], card[k], card[j]])

print(sumMax)
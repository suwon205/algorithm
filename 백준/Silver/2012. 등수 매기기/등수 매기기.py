N = int(input())
exp = []
for _ in range(N):
    exp.append(int(input()))
exp.sort()
gap = 0
for idx in range(N):
    gap += abs(exp[idx]-(idx+1))
print(gap)
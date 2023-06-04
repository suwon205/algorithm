N = list(input())
N.sort(reverse=True)
sumV = 0
for idx in N:
    sumV += int(idx)
if sumV % 3 != 0 or "0" not in N:
    print(-1)
else:
    print(''.join(N))
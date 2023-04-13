N = int(input())
lst = [0] * (N+1)
lst[1] = 1
for i in range(2,N+1):
    lst[i] = lst[i-1] + lst[i-2]
print(lst[N])
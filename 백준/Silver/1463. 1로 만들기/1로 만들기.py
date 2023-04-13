N = int(input())
lst = [0]*(N+1)

for i in range(2,N+1):
    if i % 6 == 0: #6의 배수인 경우
        lst[i] = min(lst[i//2], lst[i//3], lst[i-1])+1
    elif i % 3 == 0: #3의 배수인 경우
        lst[i] = min(lst[i//3], lst[i-1])+1
    elif i % 2 == 0:
        lst[i] = min(lst[i//2], lst[i-1])+1
    else:
        lst[i] = lst[i-1] + 1
print(lst[N])
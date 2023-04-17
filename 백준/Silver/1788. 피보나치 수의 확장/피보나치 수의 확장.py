N = int(input())
fib = [0, 1]
for i in range(2, abs(N) + 1):
    fib.append((fib[i - 1] + fib[i - 2]) % 1000000000)
if N % 2 == 0 and N < 0:
    print(-1)
elif N == 0:
    print(0)
else:
    print(1)
print(fib[abs(N)])
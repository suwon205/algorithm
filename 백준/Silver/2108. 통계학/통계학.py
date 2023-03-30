import sys
N = int(input())
lst_number = []

for _ in range(N):
    lst_number.append(int(sys.stdin.readline()))

lst_number.sort()
avg = round(sum(lst_number)/N)
mid = lst_number[N//2]
mode = {}
many_mod = []
for num in lst_number:
    if num in mode:
        mode[num] += 1
    else:
        mode[num] = 1
most = max(mode.values())

for k, v in mode.items():
    if v == most:
        many_mod.append(k)
if len(many_mod)>=2:
    mode = many_mod[1]
else:
    mode = many_mod[0]
rag = lst_number[N-1] - lst_number[0]

print(avg)
print(mid)
print(mode)
print(rag)
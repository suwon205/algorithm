N = int(input())
arr =[0] * 1001
area = 0
for _ in range(N):
    idx, h = map(int, input().split())
    arr[idx] = h
arr_first = arr[:arr.index(max(arr))+1]
maxV = max(arr_first)

for idx in range(arr_first.index(maxV)):
    if arr_first[idx] > arr_first[idx+1]:
        arr_first[idx+1] = arr_first[idx]
area += sum(arr_first)


arr_last = arr[arr.index(maxV)+1:]
while sum(arr_last) != 0:
    last_maxV = max(arr_last)
    for idx in range(arr_last.index(last_maxV)): #최대 높이까지
        arr_last[idx] = last_maxV
    area += sum(arr_last[:arr_last.index(max(arr_last))+1])
    arr_last = arr_last[arr_last.index(max(arr_last))+1:]
print(area)
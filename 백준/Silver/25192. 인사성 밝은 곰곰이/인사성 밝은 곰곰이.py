N = int(input())
data = {}
cnt = 0
for i in range(N):
    chat = input()
    if chat == 'ENTER':
        data ={}
        continue
    if chat not in data:
        data[chat] = True
        cnt += 1
print(cnt)
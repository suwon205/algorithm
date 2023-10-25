N = int(input())
lessons = []
for _ in range(N):
    st, ed = map(int, input().split())
    lessons.append((st, ed))

lessons.sort(key= lambda x : (x[1], x[0]))

select_meeting = lessons[0]
cnt = 1

for i in range(1, N):
    if lessons[i][0] >= select_meeting[1]:
        select_meeting = lessons[i]
        cnt += 1

print(cnt)
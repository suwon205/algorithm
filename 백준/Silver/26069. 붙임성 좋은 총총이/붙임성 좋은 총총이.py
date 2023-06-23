N = int(input())
# people = []
dance = [] #춤을 추고 있는 리스트
cnt = 0
flag = False
for _ in range(N):
    tmp = list(input().split())
    if 'ChongChong' in tmp:
        dance.append(tmp[0])
        dance.append(tmp[1])
        flag = True
        cnt = 2
        continue
    if flag: #총총이 등장 후
        if tmp[0] in dance: #A가 춤을 추고 있다면
            # dance.append(tmp[0])
            dance.append(tmp[1])
            cnt += 1
        if tmp[1] in dance: #B가 춤을 춘다면
            dance.append(tmp[0])
            cnt += 1
# print(len(list(set(dance))))
# print(cnt)
print(len(list(set(dance))))
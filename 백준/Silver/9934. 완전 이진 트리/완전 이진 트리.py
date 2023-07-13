#중위순회
def doit(ls, cnt):
    global Tree
    tmp = []
    if cnt != num:
        for idx in range(len(ls)):
            if idx % 2 == 0: #자식 노드의 경우
                Tree[cnt].append(ls[idx])
            else:
                tmp.append(ls[idx])
        doit(tmp, cnt + 1)

K = int(input())
ls = list(map(int, input().split()))

num = 1 #트리의 층
tmp = 1 #트리의 원소 수

while len(ls) != tmp:
    tmp += 2 ** num
    num += 1

Tree = [[] for _ in range(num)]
doit(ls, 0)
for idx in range(num-1, -1, -1):
    for i in Tree[idx]:
        print(i, end=' ')
    print()
import sys


N = int(sys.stdin.readline())
tmp =[]
for _ in range(N):
    word = sys.stdin.readline().rstrip().split()
    if word[1] == 'enter':
        tmp.append(word[0])
    elif word[1] == 'leave':
        idx = tmp.index(word[0])
        tmp.pop(idx)
tmp.sort(reverse=True)
for i in tmp:
    print(i)
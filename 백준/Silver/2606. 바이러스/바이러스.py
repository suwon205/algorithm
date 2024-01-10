from collections import deque

def find(startC):
    cnt = 0
    q = deque()
    q.append(startC)
    infection[startC] = True

    while q:
        nearC = q.popleft()
        for neighbor in computer[nearC]:
            if not infection[neighbor]:
                infection[neighbor] = True
                cnt += 1
                q.append(neighbor)
    return cnt

num = int(input())
link = int(input())
computer = [[] for _ in range(num + 1)]
for _ in range(link):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)
infection = [False] * (num + 1)
print(find(1))
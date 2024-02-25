from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()
    # db 캐시 사이즈 효율적이도록. lru 알고리즘 사용한다
    # 캐시 히트 => 1만큼 시간 든다. 없으면 5만큼 시간이 든다.
    if cacheSize == 0:
        return len(cities) * 5
    for idx in range(len(cities)):
        if idx != 0:
            if cities[idx].lower() in q:
                # print(q, "갱신 전 q", cities[idx])
                answer += 1
                cityIdx = q.index(cities[idx].lower())
                q = deque(list(q)[:cityIdx] + list(q)[cityIdx+1:])
                q.append(cities[idx].lower())
            else:
                if len(q) == cacheSize:
                    q.popleft()
                q.append(cities[idx].lower())
                answer += 5
        else:
            q.append(cities[idx].lower())
            answer += 5
        # print(q)
    return answer

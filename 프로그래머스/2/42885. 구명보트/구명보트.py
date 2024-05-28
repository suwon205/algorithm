from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while people:
        if len(people) >= 2 and people[-1] + people[0] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            people.pop()
            answer += 1
    
    return answer
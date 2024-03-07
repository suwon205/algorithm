from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while people:
        if len(people) >= 2 and people[-1] + people[0] <= limit:            
            # 가장 가벼운 사람과 가장 무거운 사람의 몸무게 합이 제한 이내인 경우
            people.pop()
            people.popleft()
            answer += 1
        else: # 무거운 사람만 태움
            people.pop()
            answer += 1
    return answer
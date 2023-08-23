def solution(targets):
    answer = 0
    bound = 0 # 격추 가능한 경계 
    targets.sort()
    for s, e in targets:
        if bound > s: # 중첩되는 경우
            bound = min(bound, e)
        else:
            bound = e
            answer += 1

    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))
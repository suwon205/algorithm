# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 오름차순 수열 만들기

def backtracking(st):
    if len(lst) == M: # 수열 완성
        if sorted(lst) == lst:
            for i in lst:
                print(i, end=' ')
            print()
    else:
        for i in range(st, N+1):
            if i not in lst:
                lst.append(i)
                backtracking(st + 1)
                lst.pop()

N, M = map(int, input().split())
lst = []
backtracking(1)
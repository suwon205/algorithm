def solution(n, lost, reserve):
    answer = 0
    for idx in range(len(reserve)):
        if reserve[idx] in lost:
            print(reserve, "잃었어요!")
            reserve.pop(idx)
        print(reserve[idx])
    return answer
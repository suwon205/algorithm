def solution(keymap, targets):
    answer = []
    dic = []
    # 딕셔너리 구현. 빠른 인덱스를 저장한다.
    for ln in range(len(keymap)):
        keymap_dict = {}
        for idx in range(len(keymap[ln])):
            if keymap[ln][idx] not in keymap_dict:
                keymap_dict[keymap[ln][idx]] = idx + 1
        dic.append(keymap_dict)


    for target in targets:
        cnt = 0
        for idx in range(len(target)): #타겟 하나하나 보기
            tmp = [] #한 문자를 확인할 때마다 초기화
            for d in dic: #딕셔너리 순회
                if target[idx] in d:
                    tmp.append(d[target[idx]])
            if tmp: #인덱스가 존재할 경우(여러 버튼 중 target[idx]를 구현할 수 있다면)
                cnt += min(tmp)
            else: #tc 2번의 경우
                cnt = -1
                break
        answer.append(cnt)
        print(answer)
    return answer

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))
# print(solution(["AA"], ["A"]))
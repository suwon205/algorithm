def solution(today, terms, privacies):
    dic = {}
    td = ''
    answer = []

    for c in today:
        if c != '.':
            td += c
    td_to_date = int(td[:4]) * 28 * 12 + int(td[4:6]) * 28 + int(td[6:])

    for term in terms:
        tmp = term.split()
        # print(tmp)
        dic[tmp[0]] = int(tmp[1]) * 28
    print(dic, '여기가 dic')
    temp = []
    idx = 1

    for pv in privacies:
        tmp = pv.split()
        date_cnt = ''
        for char in tmp[0]:
            if char != '.':
                date_cnt += char
        # print(date_cnt)
        exp = int(date_cnt[:4]) * 12 * 28 + int(date_cnt[4:6]) * 28 + int(date_cnt[6:]) + dic[tmp[1]]
        # temp.append((int(date_cnt[:4]) * 12 * 28) + (int(date_cnt[4:6] * 28) + dic[tmp[1]] + int(date_cnt[6:])))
        if td_to_date >= exp:
            answer.append(idx)
        idx += 1
    # for idx in range(len(temp)):
    #     if temp[idx] < td_to_date:
    #         answer.append(idx)

    return answer


print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution( "2020.12.17", ["A 12"], ["2010.01.01 A", "2019.12.17 A"]))
# print(solution("2019.11.01", ["A 5"], ["2019.06.01 A", "2018.01.01 A"]))
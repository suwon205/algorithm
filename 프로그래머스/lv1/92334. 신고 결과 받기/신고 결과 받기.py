
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    accept_user = {} #신고 받은 유저들을 넣어주자
    declare_user = {} #신고한 유저들을 넣어주자
    for rep in report:
        r = rep.split()
        #신고한 유저들 처리
        if r[0] in declare_user: 
            if r[1] not in declare_user[r[0]]:
                declare_user[r[0]].append(r[1])
        else:
            declare_user[r[0]] = []
            declare_user[r[0]].append(r[1])
        #신고 받은 유저들 처리
        if r[1] in accept_user:
            if r[0] not in accept_user[r[1]]:
                accept_user[r[1]].append(r[0])
        else:
            accept_user[r[1]] = []
            accept_user[r[1]].append(r[0])
    # print(accept_user, '신고 받음')
    # print(declare_user, '신고함')
    ban_user = [] #계정 정지되는 사람들 담긴다
    for acc in accept_user:
        if len(accept_user[acc]) >= k:
            ban_user.append(acc)
            
    for user in declare_user:
        # if declare_user[user] in ban_user:
        for u in declare_user[user]:
            if u in ban_user:
                answer[id_list.index(user)] += 1
    return answer

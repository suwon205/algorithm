import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a_dic = {4:0, 3:0, 2:0, 1:0}
    b_dic = {4:0, 3:0, 2:0, 1:0}
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    for idx in range(a_list[0]):
        a_dic[a_list[idx+1]] += 1
    for idx in range(b_list[0]):
        b_dic[b_list[idx+1]] += 1

    for k in range(4,0,-1):
        if a_dic[k] > b_dic[k]:
            print('A')
            break
        elif a_dic[k] < b_dic[k]:
            print('B')
            break
        if a_dic==b_dic:
            print('D')
            break
switch = int(input())

switch_list = list(input().split())

students = int(input())
for _ in range(students):
    gender, num = map(int, input().split())
    if gender == 1:
        multiple = num
        for idx in range(switch):
            if (idx+1) % multiple == 0:
                if switch_list[idx] == '1':
                    switch_list[idx] = '0'
                else:
                    switch_list[idx] = '1'
    if gender == 2:
        idx = num-1
        if switch_list[idx] == '1':
            switch_list[idx] = '0'
        else:
            switch_list[idx] = '1'
        i = 0
        while 0<=idx-1-i<switch and 0<=idx+1+i<switch and switch_list[idx-1-i] == switch_list[idx+1+i] : #좌우 대칭이 어긋나면 반복문 그만 돌기
            if switch_list[idx-1-i] =='0':
                switch_list[idx-1-i] = switch_list[idx+1+i] = '1'
            else:
                switch_list[idx-1-i] = switch_list[idx+1+i] = '0'
            i += 1

for i in range(1, (switch//20)+2):
    S = ''
    if i == (switch//20)+1:
        for idx in range(20*(i-1),switch):
            S += str(switch_list[idx])
            S += ' '
        print(S)
    else:
        for idx in range(20*(i-1),20*i):
            S += str(switch_list[idx])
            S += ' '
        print(S)
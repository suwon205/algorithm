dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

total = 0
sumV = 0
for _ in range(20):
    tmp = list(input().split())
    if tmp[2] == 'P':
        continue
    total += (float(dic[tmp[2]]) * float(tmp[1]))
    sumV += float(tmp[1])
print(total/sumV)
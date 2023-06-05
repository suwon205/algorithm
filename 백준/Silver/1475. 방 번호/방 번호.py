number = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
num = list(map(int,input()))
for n in num:
    number[n] += 1
tmp = (number[6] + number[9])
if tmp % 2 == 0:
    number[6] = tmp//2
    number[9] = tmp//2
else:
    number[6] = tmp//2
    number[9] = tmp//2 + 1
print(max(number.values()))
def op(T, lenT):
    if lenT < len(S):
        return
    if T == S and lenT == len(S):
        print(1)
        exit()
    tmp = T
    if T[-1] == 'A':
        op(T[0:-1], lenT-1)
    T = tmp
    if T[0] == 'B':
        T = T[1:]
        op(T[::-1], lenT-1)

S = list(input())
T = list(input())
lenT = len(T)
op(T,lenT)
print(0)
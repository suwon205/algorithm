def AeqB(A,cnt):
    if A>B:
        return
    elif A==B:
        print(cnt+1)
        exit()
    else:
        AeqB(A*2, cnt + 1)
        AeqB(int(str(A)+'1'), cnt +1)

A,B = map(int,input().split())
AeqB(A,0)
print(-1)
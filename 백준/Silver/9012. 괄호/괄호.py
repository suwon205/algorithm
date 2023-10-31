N = int(input())
ans = []
for _ in range(N):
    st = []
    lst = list(input())
    flag = True
    for i in lst:
        if i == '(':
            st.append('(')
        else:
            if st:
                if st[-1] == '(':
                    st.pop()
                else:
                    st.append(')')
            else:
                flag = False
                break
    if not st and flag:
        ans.append('YES')
    else:
        ans.append('NO')
for i in ans:
    print(i)
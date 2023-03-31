def whatis_wrong_ter(ln, init):
    tmp = []
    for i in range(ln):
        if maybe_trelst[i] == 0: #미지의 숫자 자릿수가 0. 1과 2 둘 다 저장해주자
            init_tmp_2 = init + 2 * (3 ** (ln-i-1))
            tmp.append(init_tmp_2)
            init_tmp_1 = init + (3 ** (ln-i-1))
            tmp.append(init_tmp_1)

        elif maybe_trelst[i] == 1: #0과 2을 저장해주어야 한다.
            init_tmp_0 = init - (3 ** (ln-i-1))
            tmp.append(init_tmp_0)
            init_tmp_2 = init + (3 ** (ln-i-1))
            tmp.append(init_tmp_2)

        else:
            init_tmp_0 = init - 2 * (3** (ln-i-1))
            tmp.append(init_tmp_0)
            init_tmp_1 = init - 1 * (3** (ln-i-1))
            tmp.append(init_tmp_1)
    return tmp


def whatis_wrong_bi(ln, init):
    tmp = []
    for i in range(ln):
        if maybe_bilst[i] == 1: #미지의 숫자 자릿수가 1인 경우. 0을 저장해주자
            init_tmp = init - 2**(ln-i-1)
            tmp.append(init_tmp)
        else:
            init_tmp = init + 2**(ln-i-1)
            tmp.append(init_tmp)
    return tmp


T = int(input())
for tc in range(1,T+1):

    maybe_bi = input()
    maybe_bilst = list(map(int,maybe_bi))
    maybe_ter = input()
    maybe_trelst = list(map(int,maybe_ter))

    binnum = int(maybe_bi,2)
    ternum = int(maybe_ter,3)

    bians = whatis_wrong_bi(len(maybe_bilst),binnum)
    treans = whatis_wrong_ter(len(maybe_trelst), ternum)
    print(f'#{tc} {list(set(bians) & set(treans))[0]}')
'''
1
1010
212
'''
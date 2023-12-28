def intToBin(arr):
    binarr = [[] for _ in range(len(arr))]
    for idx in range(len(arr)):
        binarr[idx] = bin(arr[idx])
    for idx in range(len(binarr)):
        binarr[idx] = list(binarr[idx][2:])
        if len(binarr[idx]) != len(arr):
            while len(binarr[idx]) != len(arr):
                binarr[idx].insert(0,'0')
    return binarr

def solution(n, arr1, arr2):
    arr1 = intToBin(arr1)
    arr2 = intToBin(arr2)
    ans = []
    answer = [[] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        tmp = ''
        for j in range(len(arr1)):
            if arr1[i][j] == '1' or arr2[i][j] == '1': #벽
                tmp += "#"
            else:
                tmp += " "
        ans.append(tmp)
    return ans

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
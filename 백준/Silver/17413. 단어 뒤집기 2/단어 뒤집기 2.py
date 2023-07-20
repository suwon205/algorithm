word = list(input())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호
        i += 1
        while word[i] != ">":      # 닫힌 괄호
            i += 1
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가
    elif word[i].isalnum(): # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i+=1
        tmp = word[start:i]
        tmp.reverse()
        word[start:i] = tmp
    else:                   #공백
        i+=1                

print("".join(word))
N = int(input())
word = []
ans = N
for _ in range(N):
    word.append(input())
for idx in range(N):
    tmp_dict = {}
    for i in range(len(word[idx])):
        if word[idx][i] not in tmp_dict:
            tmp_dict[word[idx][i]] = i
        elif abs(i-tmp_dict[word[idx][i]]) == 1: #연속해서 등장하는 경우
            tmp_dict[word[idx][i]] = i
        else:
            ans -= 1
            break
print(ans)
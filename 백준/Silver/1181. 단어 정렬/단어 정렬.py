sentence = []
N = int(input())
for _ in range(N):
    sentence.append(input())
sentence = list(set(sentence))
sentence.sort(key= lambda x : (len(x), x))
for word in sentence:
    print(word)
# 입력 받기
N = int(input())

# 5킬로그램 봉지로 최대한 채우는 경우를 고려
num_5kg = N // 5
num_3kg = 0
N %= 5

# 남은 설탕을 3킬로그램 봉지로 채우는 경우를 고려
while num_5kg >= 0:
    if N % 3 == 0:
        num_3kg = N // 3
        N -= 3 * num_3kg
        break
    num_5kg -= 1
    N += 5
# 결과 출력
if N == 0:
    print(num_5kg + num_3kg)
else:
    print(-1)  # 정확하게 N킬로그램을 만들 수 없는 경우

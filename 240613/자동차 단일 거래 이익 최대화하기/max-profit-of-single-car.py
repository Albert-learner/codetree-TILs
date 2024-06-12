# N = int(input())
# n_lst = list(map(int, input().split()))

# dp = [0] * N
# for i in range(N - 1):
#     dp[i] = max(n_lst[i:]) - n_lst[i]

# print(max(dp))

# 모범답안 1
# 변수 선언 및 입력:
n = int(input())
price = list(map(int, input().split()))

# 배열을 앞에서부터 순회하며 사는 시점의 후보를 선택합니다
max_profit = 0
for i in range(n):
    # 사는 시점의 다음 해부터 순회하며 파는 시점의 후보를 선택합니다
    for j in range(i + 1, n):
        profit = price[j] - price[i]

        if profit > max_profit:
            max_profit = profit
    
print(max_profit)
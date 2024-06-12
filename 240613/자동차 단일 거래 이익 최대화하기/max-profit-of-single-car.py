N = int(input())
n_lst = list(map(int, input().split()))

dp = [0] * N
for i in range(N - 1):
    dp[i] = max(n_lst[i:]) - n_lst[i]

print(max(dp))
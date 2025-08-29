n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# Please write your code here.
NEG_INF = -(10**18)
dp = [NEG_INF] * (k + 1)
ans = NEG_INF

for x in numbers:
    new_dp = [NEG_INF] * (k + 1)
    if x >= 0:
        for j in range(k + 1):
            if dp[j] != NEG_INF:
                new_dp[j] = max(new_dp[j], dp[j] + x)
        new_dp[0] = max(new_dp[0], x)
    else: 
        for j in range(1, k + 1):
            if dp[j - 1] != NEG_INF:
                new_dp[j] = max(new_dp[j], dp[j - 1] + x)
        new_dp[1] = max(new_dp[1], x)
    for j in range(k + 1):
        ans = max(ans, new_dp[j])
    dp = new_dp

print(ans)
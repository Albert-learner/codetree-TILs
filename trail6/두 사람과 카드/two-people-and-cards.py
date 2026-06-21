n = int(input())
cards = list(map(int, input().split()))

# Please write your code here.
import sys

if n <= 2:
    print(0)
    sys.exit(0)

INF = 10 ** 18
EMPTY = n

dp = [INF] * (n + 1)
dp[EMPTY] = 0

for i in range(n - 1):
    nxt = i + 1
    new_dp = [INF] * (n + 1)

    for j in range(n + 1):
        if dp[j] == INF:
            continue

        cost1 = abs(cards[i] - cards[nxt])
        new_dp[j] = min(new_dp[j], dp[j] + cost1)

        if j == EMPTY:
            cost2 = 0
        else:
            cost2 = abs(cards[j] - cards[nxt])

        new_dp[i] = min(new_dp[i], dp[j] + cost2)

    dp = new_dp

print(min(dp))
n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
total_times = sum([t for _, t in quests])

dp = [-1] * (total_times + 1)
dp[0] = 0

for e, t in quests:
    for time in range(total_times, t - 1, -1):
        if dp[time - t] != -1:
            dp[time] = max(dp[time], dp[time - t] + e)

answer = -1
for time in range(total_times + 1):
    if dp[time] >= m:
        answer = time
        break

print(answer)
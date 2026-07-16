n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
INF = 10 ** 9
size = 1 << n

dp = [[INF] * n for _ in range(size)]

dp[1][0] = 0

answer = 1

for mask in range(size):
    count = mask.bit_count()

    for last in range(n):
        prev_value = dp[mask][last]

        if prev_value == INF:
            continue

        answer = max(answer, count)

        for nxt in range(n):
            if mask & (1 << nxt):
                continue

            next_value = A[last][nxt]

            if next_value <= prev_value:
                continue

            next_mask = mask | (1 << nxt)

            if next_value < dp[next_mask][nxt]:
                dp[next_mask][nxt] = next_value

print(answer)
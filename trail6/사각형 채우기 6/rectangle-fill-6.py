n, m = map(int, input().split())

# Please write your code here.
MOD = 10007

if n > m:
    n, m = m, n

dp = [0] * (1 << n)
dp[0] = 1

def fill(row, cur_mask, next_mask, value, next_dp):
    if row == n:
        next_dp[next_mask] = (next_dp[next_mask] + value) % MOD
        return

    if cur_mask & (1 << row):
        fill(row + 1, cur_mask, next_mask, value, next_dp)
        return

    if row + 1 < n and not (cur_mask & (1 << (row + 1))):
        fill(
            row + 2,
            cur_mask,
            next_mask,
            value,
            next_dp
        )

    fill(
        row + 1,
        cur_mask,
        next_mask | (1 << row),
        value,
        next_dp
    )

for _ in range(m):
    next_dp = [0] * (1 << n)

    for mask in range(1 << n):
        if dp[mask] == 0:
            continue

        fill(0, mask, 0, dp[mask], next_dp)

    dp = next_dp

print(dp[0])
n = int(input())

# Please write your code here.
MOD = 10007

dp = [[0] * 16 for _ in range(n + 1)]
dp[0][0] = 1


def dfs(row, cur_mask, next_mask, val, col):
    if row == 4:
        dp[col + 1][next_mask] = (dp[col + 1][next_mask] + val) % MOD
        return

    if cur_mask & (1 << row):
        dfs(row + 1, cur_mask, next_mask, val, col)
        return

    if row < 3 and not (cur_mask & (1 << (row + 1))):
        dfs(
            row + 2,
            cur_mask | (1 << row) | (1 << (row + 1)),
            next_mask,
            val,
            col,
        )

    dfs(
        row + 1,
        cur_mask | (1 << row),
        next_mask | (1 << row),
        val,
        col,
    )


for col in range(n):
    for mask in range(16):
        if dp[col][mask]:
            dfs(0, mask, 0, dp[col][mask], col)

print(dp[n][0] % MOD)
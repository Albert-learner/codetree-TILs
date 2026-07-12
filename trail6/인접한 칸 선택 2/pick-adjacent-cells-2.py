n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
valid_masks = []
for mask in range(1 << n):
    if (mask & (mask << 1)) == 0:
        valid_masks.append(mask)

score = [[0] * len(valid_masks) for _ in range(m)]

for col in range(m):
    for idx, mask in enumerate(valid_masks):
        s = 0
        for row in range(n):
            if (mask >> row) & 1:
                s += board[row][col]
        score[col][idx] = s

NEG = -10 ** 18

dp = [NEG] * len(valid_masks)

for i in range(len(valid_masks)):
    dp[i] = score[0][i]

for col in range(1, m):
    ndp = [NEG] * len(valid_masks)

    for i, cur in enumerate(valid_masks):
        cur_score = score[col][i]

        for j, prev in enumerate(valid_masks):
            # 좌우 인접 금지
            if cur & prev:
                continue

            ndp[i] = max(ndp[i], dp[j] + cur_score)

    dp = ndp

print(max(dp))
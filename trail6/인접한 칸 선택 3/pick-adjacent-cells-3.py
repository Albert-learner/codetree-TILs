n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
NEG_INF = -10 ** 18

valid_masks = []
for mask in range(1 << m):
    if mask & (mask << 1) == 0:
        valid_masks.append(mask)

mask_count = {}
row_sum = [[0] * len(valid_masks) for _ in range(n)]

for idx, mask in enumerate(valid_masks):
    mask_count[mask] = mask.bit_count()

    for r in range(n):
        total = 0
        for c in range(m):
            if mask & (1 << c):
                total += board[r][c]
        row_sum[r][idx] = total

compatible = [[] for _ in range(len(valid_masks))]

for i, cur_mask in enumerate(valid_masks):
    for j, prev_mask in enumerate(valid_masks):
        if cur_mask & prev_mask == 0:
            compatible[i].append(j)

dp = [[NEG_INF] * (k + 1) for _ in range(len(valid_masks))]

zero_idx = valid_masks.index(0)
dp[zero_idx][0] = 0

for r in range(n):
    new_dp = [[NEG_INF] * (k + 1) for _ in range(len(valid_masks))]

    for cur_idx, cur_mask in enumerate(valid_masks):
        selected = mask_count[cur_mask]

        if selected > k:
            continue

        value = row_sum[r][cur_idx]

        for prev_idx in compatible[cur_idx]:
            prev_dp = dp[prev_idx]

            for cnt in range(k - selected + 1):
                if prev_dp[cnt] == NEG_INF:
                    continue

                new_cnt = cnt + selected
                candidate = prev_dp[cnt] + value

                if candidate > new_dp[cur_idx][new_cnt]:
                    new_dp[cur_idx][new_cnt] = candidate

    dp = new_dp

answer = 0

for mask_dp in dp:
    for cnt in range(k + 1):
        answer = max(answer, mask_dp[cnt])

print(answer)
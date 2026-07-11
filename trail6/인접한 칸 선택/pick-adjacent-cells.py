n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
valid_masks = []

for mask in range(1 << m):
    if mask & (mask << 1) == 0:
        valid_masks.append(mask)

empty_masks = []

for i in range(n):
    mask = 0

    for j in range(m):
        if board[i][j] == 0:
            mask |= 1 << j

    empty_masks.append(mask)

bit_count = [0] * (1 << m)

for mask in range(1, 1 << m):
    bit_count[mask] = bit_count[mask >> 1] + (mask & 1)

NEG = -10 ** 9

dp = {0: 0}

for row in range(n):
    next_dp = {}

    for cur_mask in valid_masks:
        if cur_mask & ~empty_masks[row]:
            continue

        best = NEG

        for prev_mask, value in dp.items():
            if cur_mask & prev_mask:
                continue

            best = max(best, value + bit_count[cur_mask])

        if best != NEG:
            next_dp[cur_mask] = best

    dp = next_dp

print(max(dp.values()))
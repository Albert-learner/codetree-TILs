n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def is_valid(mask):
    """같은 열 내 인접한 행이 동시에 선택되지 않음"""
    return (mask & (mask >> 1)) == 0

def col_sum(mask, col):
    """현재 열(col)에서 mask에 해당하는 칸의 합"""
    total = 0
    for row in range(n):
        if (mask >> row) & 1:
            total += board[row][col]
    return total

# 유효한 마스크 목록 미리 계산
valid_masks = [mask for mask in range(1 << n) if is_valid(mask)]

# dp[mask]: 현재 열에서 선택 패턴이 mask일 때 최대 합
INF = -1
dp = {mask: INF for mask in valid_masks}
dp[0] = 0  # 시작 전: 아무것도 선택 안 한 상태 (이전 열 없음)

for col in range(m):
    next_dp = {mask: INF for mask in valid_masks}

    for prev_mask in valid_masks:
        if dp[prev_mask] == INF:
            continue

        for cur_mask in valid_masks:
            # 이전 열과 현재 열이 같은 행을 동시에 선택하면 안 됨
            if prev_mask & cur_mask:
                continue

            val = dp[prev_mask] + col_sum(cur_mask, col)
            if val > next_dp[cur_mask]:
                next_dp[cur_mask] = val

    dp = next_dp

print(max(dp.values()))
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def is_valid(mask):
    """같은 열 내 인접한 행이 동시에 선택되지 않음"""
    return (mask & (mask >> 1)) == 0

def col_score(mask, col):
    """현재 열(col)에서 mask에 해당하는 칸의 합과 선택 수"""
    total, cnt = 0, 0
    for row in range(n):
        if (mask >> row) & 1:
            total += board[row][col]
            cnt += 1
    return total, cnt

# 유효한 마스크 목록 미리 계산
valid_masks = [mask for mask in range(1 << n) if is_valid(mask)]

INF = -1

# dp[mask][cnt]: 현재 열 패턴이 mask이고 선택 수가 cnt일 때 최대 합
dp = [[INF] * (k + 1) for _ in range(1 << n)]
dp[0][0] = 0  # 시작: 아무것도 선택 안 함

for col in range(m):
    next_dp = [[INF] * (k + 1) for _ in range(1 << n)]

    for prev_mask in valid_masks:
        for prev_cnt in range(k + 1):
            if dp[prev_mask][prev_cnt] == INF:
                continue

            for cur_mask in valid_masks:
                # 이전 열과 현재 열이 같은 행을 동시에 선택하면 안 됨
                if prev_mask & cur_mask:
                    continue

                score, cnt = col_score(cur_mask, col)
                new_cnt = prev_cnt + cnt

                if new_cnt > k:  # k개 초과하면 skip
                    continue

                val = dp[prev_mask][prev_cnt] + score
                if val > next_dp[cur_mask][new_cnt]:
                    next_dp[cur_mask][new_cnt] = val

    dp = next_dp

# 모든 mask, 모든 cnt(≤k)에서 최댓값
ans = 0
for mask in valid_masks:
    for cnt in range(k + 1):
        if dp[mask][cnt] != INF:
            ans = max(ans, dp[mask][cnt])

print(ans)
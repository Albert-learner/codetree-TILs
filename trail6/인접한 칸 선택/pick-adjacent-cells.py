n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def is_valid_row(mask, row_walls):
    """같은 행 내 인접 선택 없고, 벽 위치 선택 안 함"""
    if mask & (mask >> 1):          # 인접한 두 비트가 동시에 1이면 무효
        return False
    if mask & row_walls:            # 벽인 칸을 선택하면 무효
        return False
    return True

def no_col_conflict(mask1, mask2):
    """두 행 마스크가 같은 열을 동시에 선택하지 않음"""
    return (mask1 & mask2) == 0

MOD = 1 << m  # 사용할 비트 범위

# 각 행을 벽 비트마스크로 변환 (1인 칸 = 선택 불가)
wall_masks = []
for i in range(n):
    wm = 0
    for j in range(m):
        if board[i][j] == 1:
            wm |= (1 << j)
    wall_masks.append(wm)

# dp[mask]: 현재 행에서 선택 패턴이 mask일 때 최대 선택 수
INF = -1
dp = [INF] * (1 << m)
dp[0] = 0  # 첫 행 처리 전: 아무것도 선택 안 한 상태

for i in range(n):
    next_dp = [INF] * (1 << m)

    for prev_mask in range(1 << m):
        if dp[prev_mask] == INF:
            continue

        for cur_mask in range(1 << m):
            # 현재 행 유효성 검사
            if not is_valid_row(cur_mask, wall_masks[i]):
                continue
            # 이전 행과 열 충돌 검사
            if not no_col_conflict(prev_mask, cur_mask):
                continue

            selected = bin(cur_mask).count('1')
            val = dp[prev_mask] + selected
            if val > next_dp[cur_mask]:
                next_dp[cur_mask] = val

    dp = next_dp

print(max(dp))
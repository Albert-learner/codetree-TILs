n, m = map(int, input().split())
MOD = 10007

# n과 m 중 작은 쪽을 행(ROWS)으로 설정 → 비트마스크 상태 최소화
if n > m:
    n, m = m, n
ROWS = n  # 비트마스크 행 수 (더 작은 쪽)

def can_fill_vertical(mask):
    """
    mask: 현재 열에서 이미 채워진 행 패턴
    빈 칸(0인 비트)들을 세로(2×1) 블록으로 채울 수 있는지 확인
    연속된 빈 칸 쌍으로만 채울 수 있음
    """
    empty = (~mask) & ((1 << ROWS) - 1)
    row = 0
    while row < ROWS:
        if (empty >> row) & 1:
            if row + 1 < ROWS and (empty >> (row + 1)) & 1:
                row += 2
            else:
                return False
        else:
            row += 1
    return True

# dp[mask]: 다음 열로 mask만큼 가로 블록이 돌출된 경우의 수
dp = [0] * (1 << ROWS)
dp[0] = 1  # 초기: 돌출 없음

for col in range(m):
    next_dp = [0] * (1 << ROWS)

    for cur_mask in range(1 << ROWS):
        if dp[cur_mask] == 0:
            continue

        # cur_mask: 이전 열에서 돌출되어 이미 채워진 행들
        free = (~cur_mask) & ((1 << ROWS) - 1)  # 현재 열에서 빈 행들

        # free의 모든 부분집합 sub: 현재 열에서 가로 블록을 새로 놓을 행들
        sub = free
        while True:
            fill_mask = cur_mask | sub  # 현재 열에서 채워지는 행들

            if can_fill_vertical(fill_mask):  # 나머지를 세로 블록으로 채울 수 있는지
                next_dp[sub] = (next_dp[sub] + dp[cur_mask]) % MOD

            if sub == 0:
                break
            sub = (sub - 1) & free  # free의 다음 부분집합

    dp = next_dp

print(dp[0])
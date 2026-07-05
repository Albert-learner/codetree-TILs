n = int(input())
MOD = 10007
ROWS = 4

def can_fill_vertical(mask):
    """
    mask: 현재 열에서 이미 채워진 행 패턴
    빈 칸(0인 비트)들을 세로(2×1) 블록으로 채울 수 있는지 확인
    연속된 빈 칸 쌍으로만 채울 수 있음
    """
    empty = (~mask) & ((1 << ROWS) - 1)  # 빈 행 패턴 (4비트)
    row = 0
    while row < ROWS:
        if (empty >> row) & 1:            # 빈 칸 발견
            if row + 1 < ROWS and (empty >> (row + 1)) & 1:  # 다음 행도 빈 칸
                row += 2                  # 세로 블록으로 채움
            else:
                return False              # 홀로 남은 빈 칸 → 불가
        else:
            row += 1
    return True

# dp[mask]: 다음 열로 mask만큼 돌출된 경우의 수
dp = [0] * (1 << ROWS)
dp[0] = 1  # 초기: 돌출 없음

for col in range(n):
    next_dp = [0] * (1 << ROWS)

    for cur_mask in range(1 << ROWS):
        if dp[cur_mask] == 0:
            continue

        # cur_mask: 가로 블록이 돌출되어 이미 채워진 행들
        # free: 현재 열에서 비어있는 행들
        free = (~cur_mask) & ((1 << ROWS) - 1)

        # free의 모든 부분집합을 next_mask로 시도 (가로 블록을 새로 놓을 행들)
        sub = free
        while True:
            fill_mask = cur_mask | sub    # 현재 열에서 채워지는 행들

            # 나머지 빈 칸을 세로 블록으로 채울 수 있는지 확인
            if can_fill_vertical(fill_mask):
                next_dp[sub] = (next_dp[sub] + dp[cur_mask]) % MOD

            if sub == 0:
                break
            sub = (sub - 1) & free        # free의 다음 부분집합

    dp = next_dp

# 마지막 열 처리 후 돌출 없어야 함
print(dp[0])
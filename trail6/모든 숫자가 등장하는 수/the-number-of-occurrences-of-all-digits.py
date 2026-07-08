n = int(input())
MOD = 10007

# dp[d][mask]: 현재 마지막 숫자가 d이고, 사용된 숫자 집합이 mask인 경우의 수
FULL = (1 << 10) - 1  # 0~9 전부 사용

dp = [[0] * (1 << 10) for _ in range(10)]

# 첫 번째 자리 초기화 (0으로 시작 불가)
for d in range(1, 10):
    dp[d][1 << d] = 1

# N-1번 전이
for _ in range(n - 1):
    next_dp = [[0] * (1 << 10) for _ in range(10)]

    for d in range(10):
        for mask in range(1 << 10):
            if dp[d][mask] == 0:
                continue

            # 다음 숫자: d-1 또는 d+1
            for nd in [d - 1, d + 1]:
                if 0 <= nd <= 9:
                    next_mask = mask | (1 << nd)
                    next_dp[nd][next_mask] = (
                        next_dp[nd][next_mask] + dp[d][mask]
                    ) % MOD

    dp = next_dp

# N자리이면서 0~9 전부 등장한 경우의 수 합산
ans = 0
for d in range(10):
    ans = (ans + dp[d][FULL]) % MOD

print(ans)
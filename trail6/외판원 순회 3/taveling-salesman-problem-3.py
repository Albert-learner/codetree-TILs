n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')

# dp[mask][i]: 1번(인덱스0)에서 출발, mask 집합 방문 후 현재 i에 있는 최소 비용
# mask는 인덱스 1~n-1에 대한 비트마스크 (총 n-1비트)
dp = [[INF] * n for _ in range(1 << n)]

# 초기화: 1번 정점(인덱스 0)에서 각 정점으로 출발
for j in range(1, n):
    if A[0][j] != 0:
        dp[1 << j][j] = A[0][j]

# 전이
for mask in range(1 << n):
    # 1번 정점(비트0)은 mask에 포함되면 안 됨
    if mask & 1:
        continue

    visited = bin(mask).count('1')
    if visited >= k:  # 이미 K개 방문했으면 더 이상 확장 불필요
        continue

    for i in range(1, n):
        if not (mask >> i & 1):  # i가 방문 안 된 상태면 skip
            continue
        if dp[mask][i] == INF:
            continue

        for j in range(1, n):
            if mask >> j & 1:    # 이미 방문한 정점 skip
                continue
            if A[i][j] == 0:     # 이동 불가 skip
                continue

            next_mask = mask | (1 << j)
            new_cost = dp[mask][i] + A[i][j]
            if new_cost < dp[next_mask][j]:
                dp[next_mask][j] = new_cost

# 정확히 K개 방문한 mask 중 0번으로 귀환하는 최솟값
ans = INF
for mask in range(1 << n):
    if mask & 1:                         # 0번 정점 포함된 mask 제외
        continue
    if bin(mask).count('1') != k:        # 정확히 K개 방문한 경우만
        continue
    for i in range(1, n):
        if not (mask >> i & 1):          # 현재 위치가 mask에 포함돼야 함
            continue
        if dp[mask][i] == INF:
            continue
        if A[i][0] == 0:                 # 0번으로 귀환 불가
            continue
        ans = min(ans, dp[mask][i] + A[i][0])

print(ans)
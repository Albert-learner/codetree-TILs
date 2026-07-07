n, k = map(int, input().split())
cost = [int(input()) for _ in range(n)]
board = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')

dp = [INF] * (1 << n)
dp[0] = 0  # 아무것도 없는 초기 상태

for mask in range(1 << n):
    if dp[mask] == INF:
        continue

    # 다음에 추가할 정점 j
    for j in range(n):
        if (mask >> j) & 1:  # 이미 물체가 있으면 skip
            continue

        next_mask = mask | (1 << j)

        # 방법 1: j에 직접 물체를 놓기
        dp[next_mask] = min(dp[next_mask], dp[mask] + cost[j])

        # 방법 2: mask 안의 정점 i에서 j로 간선 연결
        for i in range(n):
            if (mask >> i) & 1:  # i에 물체가 있을 때
                dp[next_mask] = min(dp[next_mask], dp[mask] + board[i][j])

# k개 이상인 mask 중 최솟값
ans = INF
for mask in range(1 << n):
    if bin(mask).count('1') >= k:
        ans = min(ans, dp[mask])

print(ans)
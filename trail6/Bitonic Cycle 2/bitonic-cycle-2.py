n = int(input())

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# dp[i][j][k] : 둘 다 시작점에서 출발하여 서로 겹치지 않게 점을 순서대로 선택하면서
#               하나는 i번 점에 있고, 나머지 하나는 j번 점에 있고,
#               k번 거리를 0으로 계산했을 떄
#               지금까지 온 거리의 합 중 가능한 최솟값
dp = [
    [[0 for _ in range(2)] for _ in range(n)]
    for _ in range(n)
]

# x좌표 순으로 오름차순 정렬을 진행합니다.
points.sort()

# i번 점과 j번 점 사이의 거리를 계산합니다.
def dist(i, j):
    (x1, y1) = points[i]
    (x2, y2) = points[j]

    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

# 최소를 구하는 문제이므로 
# 처음에 dp값을 큰 값으로 설정합니다.
for i in range(n):
    for j in range(n):
        for k in range(2):
            dp[i][j][k] = 10**16

# 초기조건을 설정합니다.
# Bitonic Cycle 유형에서
# 둘 다 시작점인 0번 점에 서있는 순간입니다.
dp[0][0][0] = 0

# 뿌려주는 dp를 진행합니다.
# 이는 이미 값이 구해져 있다는 가정 하에서
# 그 다음 값을 갱신하는 형태입니다.
for i in range(n):
    for j in range(n):
        for k in range(2):
            # 하나는 i번 점에 있고, 나머지 하나는 j번 점에 있는 상황에서
            # 그 다음 점으로의 이동을 고민해야 합니다.

            # dp[i][j] 값이 구해져있다는 가정 하에서
            # 그 다음 상황에 해당하는 값을 갱신해야합니다.

            # Bitonic Cycle 유형의 특성상
            # max(i, j)까지는 이미 전부 해결했기에
            # max(i, j) + 1번 점을 고려해야 하는 순간입니다.
            nex = max(i, j) + 1

            # 이미 nex가 n이면 더 이상 진행하지 않습니다.
            if nex == n:
                continue
            
            # i번 점을 nex로 이동하는 경우입니다.
            # 이 경우에는 i번 점과 nex점 간의 거리만큼 더 더해줘야 합니다.
            # 이 경우를 기존 값과 비교하여 최솟값을 적어줍니다.
            dp[nex][j][k] = min(dp[nex][j][k], dp[i][j][k] + dist(i, nex))
            # 혹은 이번 이동에서 두 점 사이의 거리를 0으로 계산할 수도 있습니다.
            if k == 0:
                dp[nex][j][k + 1] = min(dp[nex][j][k + 1], dp[i][j][k])

            # j번 점을 nex로 이동하는 경우입니다.
            # 이 경우에는 j번 점과 nex점 간의 거리만큼 더 더해줘야 합니다.
            # 이 경우를 기존 값과 비교하여 최솟값을 적어줍니다.
            dp[i][nex][k] = min(dp[i][nex][k], dp[i][j][k] + dist(j, nex))
            # 혹은 이번 이동에서 두 점 사이의 거리를 0으로 계산할 수도 있습니다.
            if k == 0:
                dp[i][nex][k + 1] = min(dp[i][nex][k + 1], dp[i][j][k])

# 여기서의 답은 둘 다 n - 1번 점으로 도착했을 상황이므로
# 한 쪽이 n - 1인 경우에 대해서 
# 다른 한 쪽을 n - 1로 바로 연결시켜주는 경우 중 최솟값을 구해줍니다.
# 문제 특성상 dp[i][j]는 dp[j][i]와 값이 같을 것이므로
# 답 계산시 한쪽만 고려해도 됩니다.
ans = 10**16
for i in range(n):
    # 이미 두 점 사이의 거리를 0으로 계산한 경우의 정답의 최솟값을 갱신해줍니다.
    ans = min(ans, dp[i][n - 1][1] + dist(i, n - 1))

    # 아직 두 점 사이의 거리를 0으로 계산하지 않은 경우의 정답의 최솟값을 갱신해줍니다.
    ans = min(ans, dp[i][n - 1][0])

print(ans)

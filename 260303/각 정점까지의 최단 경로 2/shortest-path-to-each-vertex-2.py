import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

# dist 초기값을 전부 아주 큰 값으로 설정
dist = [
    [INT_MAX] * (n + 1)
    for _ in range(n + 1)
]

# 자기 자신으로 가는 값은 0으로 설정해줘야 함에 유의합니다.
for i in range(1, n + 1):
    dist[i][i] = 0

# 그래프를 인접행렬로 표현
for _ in range(m):
    x, y, z = tuple(map(int, input().split()))
    # x -> y 간선이
    # 여러 개 주어질 수도 있다고 하였으므로
    # 최솟값을 계속 갱신해줍니다.
    dist[x][y] = min(dist[x][y], z)

for k in range(1, n + 1): # 확실하게 거쳐갈 정점을 1번부터 N번까지 순서대로 정의합니다.
    for i in range(1, n + 1): # 고정된 k에 대해 모든 쌍 (i, j)를 살펴봅니다.
        for j in range(1, n + 1):
            # i에서 j로 가는 거리가 k를 경유해 가는 것이 더 좋다면
            # dist[i][j]값을 갱신해줍니다.
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 모든 쌍에 대한 최단거리 결과를 출력합니다.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 불가능한 경우에는 -1을 출력합니다.
        if dist[i][j] == INT_MAX:
            print(-1, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()

import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, m, p, q = tuple(map(int, input().split()))

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
    dist[x][y] = z

for k in range(1, n + 1): # 확실하게 거쳐갈 정점을 1번부터 N번까지 순서대로 정의합니다.
    for i in range(1, n + 1): # 고정된 k에 대해 모든 쌍 (i, j)를 살펴봅니다.
        for j in range(1, n + 1):
            # i에서 j로 가는 거리가 k를 경유해 가는 것이 더 좋다면
            # dist[i][j]값을 갱신해줍니다.
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

ans = 0
cnt = 0

# q개의 질문에 대해 최단 거리를 답변합니다.
for _ in range(q):
    x, y = tuple(map(int, input().split()))

    distance = INT_MAX
    # 모든 p개의 빨간 점에 대해, 이동 가능한지 확인합니다.
    for i in range(1, p + 1):
        distance = min(distance, dist[x][i] + dist[i][y])

    # 만약 이동 불가능하다면, 넘어갑니다.
    if distance >= INT_MAX:
        continue
        
    ans += distance
    cnt += 1

print(cnt)
print(ans)

import sys

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

# 그래프를 인접행렬로 표현합니다.
# dist에 입력을 받아줍니다.
dist = [
    list(map(int, input().split()))
    for _ in range(n)
]

for k in range(n): # 확실하게 거쳐갈 정점을 1번부터 N번까지 순서대로 정의합니다.
    for i in range(n): # 고정된 k에 대해 모든 쌍 (i, j)를 살펴봅니다.
        for j in range(n):
            # i에서 j로 가는 거리가 k를 경유해 가는 것이 더 좋다면
            # dist[i][j]값을 갱신해줍니다.
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# m개의 질문에 대해 최단 거리를 답변합니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    # 모든 쌍에 대한 최단거리 결과를 가지고 있기 때문에,
    # 어느 경로를 질문하더라도 바로 최단거리를 출력할 수 있습니다.
    print(dist[x - 1][y - 1])

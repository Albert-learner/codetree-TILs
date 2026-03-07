# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    # x > y가 확실하므로 1을 적어줍니다.
    graph[x][y] = 1

for k in range(1, n + 1): # 확실하게 거쳐갈 정점을 1번부터 N번까지 순서대로 정의합니다.
    for i in range(1, n + 1): # 고정된 k에 대해 모든 쌍 (i, j)를 살펴봅니다.
        for j in range(1, n + 1):
            # i -> k, k -> j로 가능 길이 있다면
            # i -> j도 가능하다는 뜻입니다.
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# 각 정수마다
# 크기 비교 결과를 추론할 수 없는 정수의 개수를 출력합니다.
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if i == j:
            continue
        if graph[i][j] or graph[j][i]: # 둘 중 누가 큰지 알 수 있는 경우라면
            continue                   # 패스합니다.
        cnt += 1
    print(cnt)

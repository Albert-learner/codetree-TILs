# 변수 선언 및 입력:
n = int(input())
graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]
for i in range(1, n + 1):
    graph[i] = [0] + list(map(int, input().split()))
    
# i -> i로는 갈 수 있다고 전부 표시를 해줘야 합니다.
for i in range(1, n + 1):
    graph[i][i] = 1

for k in range(1, n + 1): # 확실하게 거쳐갈 정점을 1번부터 N번까지 순서대로 정의합니다.
    for i in range(1, n + 1): # 고정된 k에 대해 모든 쌍 (i, j)를 살펴봅니다.
        for j in range(1, n + 1):
            # i -> k, k -> j로 가능 길이 있다면
            # i -> j도 가능하다는 뜻입니다.
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

# 모든 쌍에 대한 이동 가능 결과를 출력합니다.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=" ")
    print()

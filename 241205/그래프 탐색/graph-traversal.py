N, M = map(int, input().split())

graph = [[0] * N for _ in range(N)]
paths = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
visited = [False] * M

for start, end in paths:
    graph[start][end] = 1

def DFS(vertex):
    for curr_v in range(1, M + 1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            print(curr_v)
            visited[curr_v] = True
            DFS(curr_v)

DFS(1)
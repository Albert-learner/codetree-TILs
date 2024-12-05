N, M = map(int, input().split())

graph = [[0] * N for _ in range(N)]
paths = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
visited = [False] * (N + 1)

for start, end in paths:
    graph[start][end] = 1
    graph[end][start] = 1

def DFS(vertex):
    cnt = 1
    for cur_v in range(len(graph[vertex])):
        if graph[vertex][cur_v] == 1 and visited[cur_v + 1] == False:
            visited[cur_v + 1] = True
            cnt += DFS(cur_v)
    return cnt

visited[1] = True
print(DFS(0) - 1)

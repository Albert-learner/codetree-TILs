n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for v1, v2 in edges:
    graph[v1].append(v2)
    graph[v2].append(v1)

def DFS(v):
    for oth_v in graph[v]:
        if not visited[oth_v]:
            visited[oth_v] = True
            DFS(oth_v)

st_v = 1
visited[st_v] = True
DFS(st_v)

v_cnts = 0
for i in range(1, n + 1):
    if visited[i]:
        v_cnts += 1

print(v_cnts - 1)
    

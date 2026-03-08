n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
graph = [[] for _ in range(n + 1)]

for a, b, d in edges:
    graph[a].append((b, d))
    graph[b].append((a, d))

def DFS(start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    stack = [start]

    while stack:
        cur = stack.pop()
        for nxt, d in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + d
                stack.append(nxt)

    far_node = nxt
    far_dist = 0
    for i in range(1, n + 1):
        if dist[i] > far_dist:
            far_dist = dist[i]
            far_node = i

    return far_node, far_dist

far_node, _ = DFS(1)
_, diameter = DFS(far_node)
print(diameter)

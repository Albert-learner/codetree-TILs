n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
graph = [[] for _ in range(n + 1)]
for a, b, w in edges:
    graph[a].append((b, w))
    graph[b].append((a, w))

def farthest(start):
    dist = [-1] * (n + 1)
    dist[start] = 0
    stack = [start]

    while stack:
        cur = stack.pop()
        for nxt, w in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + w
                stack.append(nxt)

    far_node = start
    far_dist = 0
    for i in range(1, n + 1):
        if dist[i] > far_dist:
            far_dist = dist[i]
            far_node = i

    return far_node, far_dist

u, _ = farthest(1)
_, answer = farthest(u)

print(answer)
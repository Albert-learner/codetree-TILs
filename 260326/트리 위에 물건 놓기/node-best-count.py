n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
order = []

stack = [1]
parent[1] = -1

while stack:
    cur = stack.pop()
    order.append(cur)
    for nxt in graph[cur]:
        if nxt == parent[cur]:
            continue
        parent[nxt] = cur
        stack.append(nxt)

dp0 = [0] * (n + 1)
dp1 = [0] * (n + 1)

for cur in reversed(order):
    dp1[cur] = 1 
    dp0[cur] = 0

    for nxt in graph[cur]:
        if nxt == parent[cur]:
            continue

        dp1[cur] += min(dp0[nxt], dp1[nxt])

        dp0[cur] += dp1[nxt]

print(min(dp0[1], dp1[1]))
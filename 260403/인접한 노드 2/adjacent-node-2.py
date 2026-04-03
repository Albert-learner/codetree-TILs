n = int(input())

value = [0] + list(map(int, input().split()))
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
    dp1[cur] = value[cur]
    for nxt in graph[cur]:
        if nxt == parent[cur]:
            continue

        dp0[cur] += max(dp0[nxt], dp1[nxt])
        dp1[cur] += dp0[nxt]

selected = []
def trace(root, parent_selected):
    stack = [(root, parent_selected, 0)]
    while stack:
        node, psel, state = stack.pop()

        if state == 0:
            if psel:
                take = False
            else:
                take = dp1[node] > dp0[node]

            if take:
                selected.append(node)

            stack.append((node, take, 1))

            children = []
            for nxt in graph[node]:
                if nxt == parent[node]:
                    continue

                children.append(nxt)

            for nxt in reversed(children):
                stack.append((nxt, take, 0))

trace(1, False)

selected.sort()
print(max(dp0[1], dp1[1]))
print(*selected)
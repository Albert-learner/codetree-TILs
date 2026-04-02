n = int(input())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
value = [0] + [int(input()) for _ in range(n)]

# Please write your code here.
import sys

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

down = [0] * (n + 1)

answer = -10**18

for cur in reversed(order):
    best1, best2 = 0, 0
    for nxt in graph[cur]:
        if nxt == parent[cur]:
            continue

        contrib = max(0, down[nxt])

        if contrib > best1:
            best2 = best1
            best1 = contrib
        elif contrib > best2:
            best2 = contrib

    down[cur] = value[cur] + best1

    path_sum = value[cur] + best1 + best2
    answer = max(answer, path_sum)

print(answer)
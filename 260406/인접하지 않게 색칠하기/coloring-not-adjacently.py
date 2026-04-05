n = int(input())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
value = [int(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
import sys
sys.setrecursionlimit(200000)

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

val = [0] + value

parent = [0] * (n + 1)
order = []
stack = [1]
parent[1] = -1

while stack:
    u = stack.pop()
    order.append(u)
    for v in graph[u]:
        if v == parent[u]:
            continue

        parent[v] = u
        stack.append(v)

NEG = -10 ** 18

dp0 = [None] * (n + 1)
dp1 = [None] * (n + 1)
subsz = [0] * (n + 1)

for u in reversed(order):
    cur0 = [NEG] * (k + 1)
    cur1 = [NEG] * (k + 1)

    cur0[0] = 0

    if k >= 1:
        cur1[1] = val[u]

    current_size = 1

    for v in graph[u]:
        if v == parent[u]:
            continue

        child0 = dp0[v]
        child1 = dp1[v]
        child_size = subsz[v]

        new0 = [NEG] * (k + 1)
        new1 = [NEG] * (k + 1)

        max_i = min(current_size, k)
        max_j = min(child_size, k)

        for i in range(max_i + 1):
            for j in range(max_j + 1):
                if i + j > k:
                    continue

                best_child = max(child0[j], child1[j])
                if cur0[i] != NEG and best_child != NEG:
                    new0[i + j] = max(new0[i + j], cur0[i] + best_child)

                if cur1[i] != NEG and child0[j] != NEG:
                    new1[i + j] = max(new1[i + j], cur1[i] + child0[j])

        cur0 = new0
        cur1 = new1
        current_size = min(k, current_size + child_size)

    dp0[u] = cur0
    dp1[u] = cur1
    subsz[u] = current_size

answer = 0
for t in range(k + 1):
    answer = max(answer, dp0[1][t], dp1[1][t])

print(answer)
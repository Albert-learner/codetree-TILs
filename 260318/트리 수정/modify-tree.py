n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
from_v, to_v, weight = zip(*edges)
from_v = list(from_v)
to_v = list(to_v)
weight = list(weight)

# Please write your code here.
import sys
sys.setrecursionlimit(200000)

graph = [[] for _ in range(n)]
for a, b, w in edges:
    graph[a].append((b, w))
    graph[b].append((a, w))

root = 0
parent = [-1] * n
pw = [0] * n                  
order = []

stack = [root]
parent[root] = root
while stack:
    u = stack.pop()
    order.append(u)
    for v, w in graph[u]:
        if parent[v] != -1:
            continue
        parent[v] = u
        pw[v] = w
        stack.append(v)

parent[root] = -1

children = [[] for _ in range(n)]
for v in range(n):
    if parent[v] != -1:
        children[parent[v]].append((v, pw[v]))

down = [0] * n
sub_diam = [0] * n

for u in reversed(order):
    best1 = 0
    best2 = 0
    diam = 0

    for v, w in children[u]:
        arm = down[v] + w
        if arm >= best1:
            best2 = best1
            best1 = arm
        elif arm > best2:
            best2 = arm

        if sub_diam[v] > diam:
            diam = sub_diam[v]

    down[u] = best1
    sub_diam[u] = max(diam, best1 + best2)

NEG = -10**18
up_dist = [NEG] * n
up_diam = [0] * n

for u in order:
    for v, w_uv in children[u]:
        arms = [0] 

        if up_dist[u] != NEG:
            arms.append(up_dist[u])

        max_part_diam = up_diam[u]

        for s, w_us in children[u]:
            if s == v:
                continue
            arms.append(down[s] + w_us)
            if sub_diam[s] > max_part_diam:
                max_part_diam = sub_diam[s]

        arms.sort(reverse=True)
        if len(arms) == 1:
            through_u = arms[0]
        else:
            through_u = arms[0] + arms[1]

        up_diam[v] = max(max_part_diam, through_u)

        up_dist[v] = w_uv + arms[0]

answer = 0
for v in range(n):
    if parent[v] == -1:
        continue

    answer = max(answer, sub_diam[v] + pw[v] + up_diam[v])

print(answer)
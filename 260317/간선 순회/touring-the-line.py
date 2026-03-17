n, d = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
from_v, to_v, length = zip(*edges)
from_v = list(from_v)
to_v = list(to_v)
length = list(length)

# Please write your code here.
import sys
sys.setrecursionlimit(200000)

graph = [[] for _ in range(n + 1)]
for a, b, w in edges:
    graph[a].append((b, w))
    graph[b].append((a, w))

parent = [0] * (n + 1)
order = []

stack = [1]
parent[1] = -1
while stack:
    cur = stack.pop()
    order.append(cur)
    for nxt, _ in graph[cur]:
        if nxt == parent[cur]:
            continue
        parent[nxt] = cur
        stack.append(nxt)

down_edges = [0] * (n + 1)
down_weight = [0] * (n + 1)

def better(e1, w1, e2, w2):
    if e1 != e2:
        return e1 > e2
    return w1 < w2

best_edges = -1
best_weight = 10**18

for node in reversed(order):
    top1_e, top1_w = -1, 10**18
    top2_e, top2_w = -1, 10**18

    for nxt, w in graph[node]:
        if nxt == parent[node]:
            continue

        cand_e = down_edges[nxt] + 1
        cand_w = down_weight[nxt] + w

        if better(cand_e, cand_w, top1_e, top1_w):
            top2_e, top2_w = top1_e, top1_w
            top1_e, top1_w = cand_e, cand_w
        elif better(cand_e, cand_w, top2_e, top2_w):
            top2_e, top2_w = cand_e, cand_w

    if top1_e != -1:
        down_edges[node] = top1_e
        down_weight[node] = top1_w
    else:
        down_edges[node] = 0
        down_weight[node] = 0

    if better(down_edges[node], down_weight[node], best_edges, best_weight):
        best_edges = down_edges[node]
        best_weight = down_weight[node]

    if top2_e != -1:
        path_e = top1_e + top2_e
        path_w = top1_w + top2_w
        if better(path_e, path_w, best_edges, best_weight):
            best_edges = path_e
            best_weight = path_w

print((best_weight + d - 1) // d)
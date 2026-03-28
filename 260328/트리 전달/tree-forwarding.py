n, m = map(int, input().split())

# 1-based indexing for parent array
parent = [-1] + list(map(int, input().split()))

# Store operations in separate lists with 1-based indexing
i = [-1]  # node indices
w = [-1]  # weights
for _ in range(m):
    node, weight = map(int, input().split())
    i.append(node)
    w.append(weight)

# Please write your code here.
import sys

children = [[] for _ in range(n + 1)]
for node in range(2, n + 1):
    children[parent[node]].append(node)

score = [0] * (n + 1)

for idx in range(1, m + 1):
    score[i[idx]] += w[idx]

stack = [1]
while stack:
    cur = stack.pop()
    for nxt in children[cur]:
        score[nxt] += score[cur]
        stack.append(nxt)

print(*score[1:])
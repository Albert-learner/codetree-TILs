n = int(input())
values = [0] + list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
import sys

if n == 1:
    print(0)
    sys.exit()

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

balance = [0] * (n + 1)
answer = 0

for cur in reversed(order):
    balance[cur] += values[cur] - 1
    answer += abs(balance[cur])

    if parent[cur] != -1:
        balance[parent[cur]] += balance[cur]

answer -= abs(balance[1])

print(answer)
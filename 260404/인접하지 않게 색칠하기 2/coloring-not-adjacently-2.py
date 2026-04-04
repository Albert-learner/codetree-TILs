n = int(input())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
from_nodes, to_nodes = zip(*edges)
from_nodes = list(from_nodes)
to_nodes = list(to_nodes)

a = [0] + [int(input()) for _ in range(n)]

k = int(input())

# Please write your code here.
adj = [[] for _ in range(n + 1)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

NEG = -10**18

dp0 = {}
dp1 = {}

stack = [(1, 0, 0)]

while stack:
    u, parent, state = stack.pop()

    if state == 0:
        stack.append((u, parent, 1))
        for v in adj[u]:
            if v != parent:
                stack.append((v, u, 0))
    else:
        children = [v for v in adj[u] if v != parent]

        not_selected = [NEG] * (k + 1)
        not_selected[0] = 0

        selected = [NEG] * (k + 1)
        if k >= 1:
            selected[1] = a[u]

        for c in children:
            child0 = dp0[c]
            child1 = dp1[c]

            child_best = [max(child0[i], child1[i]) for i in range(k + 1)]

            new_not_selected = [NEG] * (k + 1)
            new_selected = [NEG] * (k + 1)

            for i in range(k + 1):
                if not_selected[i] == NEG:
                    continue
                for j in range(k - i + 1):
                    if child_best[j] == NEG:
                        continue
                    val = not_selected[i] + child_best[j]
                    if val > new_not_selected[i + j]:
                        new_not_selected[i + j] = val

            for i in range(k + 1):
                if selected[i] == NEG:
                    continue
                for j in range(k - i + 1):
                    if child0[j] == NEG:
                        continue
                    val = selected[i] + child0[j]
                    if val > new_selected[i + j]:
                        new_selected[i + j] = val

            not_selected = new_not_selected
            selected = new_selected

            del dp0[c]
            del dp1[c]

        dp0[u] = not_selected
        dp1[u] = selected

answer = 0
for t in range(k + 1):
    answer = max(answer, dp0[1][t], dp1[1][t])

print(answer)
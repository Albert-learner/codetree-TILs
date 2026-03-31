n = int(input())
values = [0] + list(map(int, input().split()))
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
    u = stack.pop()
    order.append(u)
    for v in graph[u]:
        if v == parent[u]:
            continue

        parent[v] = u
        stack.append(v)

INF = 10 ** 18
dp0 = [-INF] * (n + 1)
dp1 = [-INF] * (n + 1)
dp2 = [-INF] * (n + 1)

for u in reversed(order):
    children = [v for v in graph[u] if v != parent[u]]

    total0 = values[u]
    for v in children:
        total0 += dp2[v]
    dp0[u] = total0

    total2 = 0
    possible2 = True
    for v in children:
        best = max(dp0[v], dp1[v])   
        if best <= -INF // 2:
            possible2 = False
            break
        total2 += best
    dp2[u] = total2 if possible2 else -INF

    if not children:
        dp1[u] = -INF
    else:
        base = 0
        selected_exists = False
        extra_cost = INF
        possible1 = True

        for v in children:
            a = dp0[v]
            b = dp1[v]

            best = max(a, b)
            if best <= -INF // 2:
                possible1 = False
                break

            base += best
            if a >= b:
                selected_exists = True
            else:
                extra_cost = min(extra_cost, b - a)

        if not possible1:
            dp1[u] = -INF
        elif selected_exists:
            dp1[u] = base
        else:
            dp1[u] = base - extra_cost  

print(max(dp0[1], dp1[1]))
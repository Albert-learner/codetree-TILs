m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import defaultdict, deque

nodes = set()
indegree = defaultdict(int)
graph = defaultdict(list)

for a, b in edges:
    nodes.add(a)
    nodes.add(b)
    graph[a].append(b)
    indegree[b] += 1
    if a not in indegree:
        indegree[a] = indegree[a]

roots = [node for node in nodes if indegree[node] == 0]

if len(roots) != 1:
    print(0)
else:
    root = roots[0]
    is_tree = True

    for node in nodes:
        if node == root:
            continue

        if indegree[node] != 1:
            is_tree = False
            break

    if is_tree:
        visited = set()
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            
            visited.add(cur)
            for nxt in graph[cur]:
                if nxt not in visited:
                    stack.append(nxt)

        if len(visited) != len(nodes):
            is_tree = False

    print(1 if is_tree else 0)
n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*edges)
a, b = list(a), list(b)

# Please write your code here.
import sys

MAX_NODE = 100000

parent = list(range(MAX_NODE + 1))
size = [1] * (MAX_NODE + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(x, y):
    fx, fy = find(x), find(y)

    if fx == fy:
        return

    if size[fx] < size[fy]:
        fx, fy = fy, fx

    parent[fy] = fx
    size[fx] += size[fy]

    return size[fx]

answer = []
for x, y in edges:
    component_size = union(x, y)
    answer.append(str(component_size))

print("\n".join(answer))
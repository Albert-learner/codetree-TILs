n = int(input())
nodes = input().split()
m = int(input())

# Please write your code here.
from array import array

nodes.sort()
idx = {name: i for i, name in enumerate(nodes)}

ancestor_count = [0] * n

child_list = array('H')
ancestor_list = array('H')

for _ in range(m):
    x, y = input().split()

    child = idx[x]
    ancestor = idx[y]

    child_list.append(child)
    ancestor_list.append(ancestor)

    ancestor_count[child] += 1

parent = [-1] * n
best_depth = [-1] * n

for child, ancestor in zip(child_list, ancestor_list):
    if ancestor_count[ancestor] > best_depth[child]:
        best_depth[child] = ancestor_count[ancestor]
        parent[child] = ancestor

children = [[] for _ in range(n)]
roots = []

for i in range(n):
    if parent[i] == -1:
        roots.append(i)
    else:
        children[parent[i]].append(i)

for i in range(n):
    children[i].sort()

print(len(roots))
print(*[nodes[i] for i in roots])

for i in range(n):
    result = [nodes[i], str(len(children[i]))]
    for child in children[i]:
        result.append(nodes[child])
    print(" ".join(result))
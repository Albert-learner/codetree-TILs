n = int(input())

from_nodes = []
to_nodes = []
for _ in range(n - 1):
    f, t = map(int, input().split())
    from_nodes.append(f)
    to_nodes.append(t)

a, b = map(int, input().split())

# Please write your code here.
parent = [0] * (n + 1)

for i in range(n - 1):
    parent[to_nodes[i]] = from_nodes[i]

visited = [False] * (n + 1)
cur = a
while cur != 0:
    visited[cur] = True
    cur = parent[cur]

cur = b
while cur != 0:
    if visited[cur]:
        print(cur)
        break
    
    cur = parent[cur]

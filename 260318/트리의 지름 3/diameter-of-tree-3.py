n = int(input())
edges = [[] for _ in range(n + 1)]

# Please write your code here.
import sys
sys.setrecursionlimit(100000)

for i in range(n - 1):
    a, b, w = map(int, input().split())
    edges[a].append((b, w))
    edges[b].append((a, w))

visited = [False for i in range(n + 1)]
dist_list = [0 for i in range(n + 1)]
max_dist = 0
last_node = 0
a, b, ans = 0, 0, 0

def dfs(cur,ignore):
    global max_dist, last_node
    visited[cur] = True
    for next, dist in edges[cur]:
        if not visited[next]:
            dist_list[next] = dist_list[cur] + dist

            if dist_list[next] > max_dist and next != ignore:
                max_dist = dist_list[next]
                last_node = next

            dfs(next,ignore)

dfs(1,-1)
a = last_node

visited = [False for i in range(n + 1)]
dist_list = [0 for i in range(n + 1)]
max_dist = -1

dfs(a,-1)
b = last_node

visited = [False for i in range(n + 1)]
dist_list = [0 for i in range(n + 1)]
max_dist = -1

dfs(a,b)
ans = max(ans,max_dist)

visited = [False for i in range(n + 1)]
dist_list = [0 for i in range(n + 1)]
max_dist = -1

dfs(b,a)
ans = max(ans,max_dist)

print(ans)

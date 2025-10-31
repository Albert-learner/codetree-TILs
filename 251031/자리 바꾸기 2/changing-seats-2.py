n, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
pos2person = list(range(n + 1))

vis = [set() for _ in range(n + 1)]
for i in range(1, n + 1):
    vis[i].add(i)

for a, b in edges:
    pa, pb = pos2person[a], pos2person[b]
    vis[pa].add(b)
    vis[pb].add(a)
    pos2person[a], pos2person[b] = pb, pa

nxt = [0] * (n + 1)
for seat in range(1, n + 1):
    person = pos2person[seat]
    nxt[person] = seat

for i in range(1, n + 1):
    s1 = i
    s2 = nxt[s1]
    s3 = nxt[s2]
    reachable = set()
    reachable |= vis[s1]
    reachable |= vis[s2]
    reachable |= vis[s3]
    print(len(reachable))
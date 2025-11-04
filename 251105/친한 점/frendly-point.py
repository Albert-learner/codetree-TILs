n, m = map(int, input().split())

# Store points as list of tuples
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries as list of tuples
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from sortedcontainers import SortedSet

sset = SortedSet()
for x, y in points:
    sset.add((x, y))

for qx, qy in queries:
    friendly_point_idx = sset.bisect_left((qx, qy))
    if friendly_point_idx < len(sset):
        friendly_point = sset[friendly_point_idx]
        fx, fy = friendly_point
        print(fx, fy)
    else:
        print(-1, -1)

n, m = map(int, input().split())

# Store points as list of tuples (x, y)
points = [tuple(map(int, input().split())) for _ in range(n)]

# Store queries
queries = [int(input()) for _ in range(m)]

# Please write your code here.
from sortedcontainers import SortedSet

sset = SortedSet(points)
NEG_INF = -10 ** 20

for query in queries:
    idx = sset.bisect_left((query, NEG_INF))
    if idx == len(sset):
        print(-1, -1)
    else:
        x, y = sset[idx]
        print(x, y)
        sset.remove((x, y))
    

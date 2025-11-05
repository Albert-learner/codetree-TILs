n = int(input())
queries = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet

dists = []
sset = SortedSet([0])
for q in queries:
    sset.add(q)
    c_idx = sset.index(q)
    left_val, right_val = 0, 0

    if c_idx > 0:
        left_val = sset[c_idx - 1]
        dists.append(q - left_val)
    
    if c_idx < len(sset) - 1:
        right_val = sset[c_idx + 1]
        dists.append(right_val - q)

    print(min(dists))

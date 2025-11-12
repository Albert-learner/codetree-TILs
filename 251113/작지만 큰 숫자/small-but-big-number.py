n, m = map(int, input().split())
sequence = list(map(int, input().split()))
queries = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet

sset = SortedSet(sequence)
for query in queries:
    ridx = sset.bisect_left(query)

    if ridx == 0:
        print(-1)
        continue
        
    if sset[ridx] > query:
        ridx -= 1
    print(sset[ridx])
    sset.remove(sset[ridx])
    
    
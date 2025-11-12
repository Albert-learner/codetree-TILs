n, m = map(int, input().split())
sequence = list(map(int, input().split()))
queries = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedList

slst = SortedList(sequence)
for query in queries:
    ridx = slst.bisect_right(query) - 1

    if ridx < 0:
        print(-1)
    else:
        val = slst[ridx]
        print(val)
        slst.pop(ridx)
    
    

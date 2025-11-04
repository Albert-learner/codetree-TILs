n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
from sortedcontainers import SortedSet

sset = SortedSet(arr)
for num in queries:
    idx = sset.bisect_left(num)
    if idx == len(sset):
        print(-1)
    else:
        print(sset[idx])
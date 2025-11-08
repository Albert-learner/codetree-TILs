n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
from sortedcontainers import SortedSet
import sys

sset = SortedSet(arr)
INT_MAX = sys.maxsize
ans = INT_MAX

for num in arr:
    min_idx = sset.bisect_left(m + num)
    if min_idx != len(sset):
        ans = min(ans, sset[min_idx] - num)

    max_idx = sset.bisect_right(num - m) - 1
    if max_idx >= 0:
        ans = min(ans, num - sset[max_idx])

if ans == INT_MAX:
    ans = -1

print(ans)
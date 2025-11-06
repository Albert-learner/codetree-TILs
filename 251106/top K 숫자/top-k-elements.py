n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from sortedcontainers import SortedSet

sset = sorted(SortedSet(arr), reverse = True)
print(*sset[:k])
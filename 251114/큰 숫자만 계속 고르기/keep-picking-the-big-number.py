n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from collections import deque

arr = sorted(deque(arr))
while m > 0:
    max_cst, max_cst_idx = arr[-1], -1
    arr[max_cst_idx] -= 1

    arr = sorted(arr)
    m -= 1

print(max(arr))
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from collections import defaultdict

cnts = defaultdict(int)
l, ans, over = 0, 0, 0

for r in range(n):
    x = arr[r]
    cnts[x] += 1
    if cnts[x] == k + 1:
        over += 1

    while over > 0:
        y = arr[l]
        if cnts[y] == k + 1:
            over -= 1
        cnts[y] -= 1
        l += 1

    ans = max(ans, r - l + 1)

print(ans)
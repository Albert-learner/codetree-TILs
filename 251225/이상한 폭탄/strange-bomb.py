n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
from collections import Counter

bombs = []

for idx in range(len(arr) - k):
    i_num = arr[idx]
    valid_cntr = Counter(arr[idx:idx + k + 1])
    if valid_cntr[i_num] >= 2:
        bombs.append(i_num)

if len(bombs) == 0:
    print(-1)
else:
    print(max(bombs))


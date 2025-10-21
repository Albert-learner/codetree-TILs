n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from collections import defaultdict

arr_dict = defaultdict(int)
for num in arr:
    arr_dict[num] += 1

k_cnts = 0
for num in set(arr):
    v = arr_dict[num]
    k2 = k - num
    if num == k2:
        result = v * (v - 1)
    else:
        result = v * arr_dict[k2]

    k_cnts += result

print(k_cnts // 2)
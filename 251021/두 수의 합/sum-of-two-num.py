n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations

k_cnts = 0
arr_combs = list(combinations(arr, 2))
for arr_comb in arr_combs:
    if sum(arr_comb) == k:
        k_cnts += 1

print(k_cnts)
n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
from itertools import combinations
from functools import reduce

combs_lst = list(combinations(A, m))

max_xor = 0
for comb in combs_lst:
    xor = reduce(lambda x, y: x ^ y, comb)
    max_xor = max(max_xor, xor)

print(max_xor)
n = int(input())
num = list(map(int, input().split()))

# Please write your code here.
import sys
from itertools import combinations

half = len(num) // 2
min_sum_diff = sys.maxsize
combs_lst = list(combinations(num, half))

half_combs = []
seen = set()
for comb in combs_lst:
    left = list(comb)
    right = [x for x in num if x not in left]
    key = tuple(sorted(left))
    if key not in seen:
        half_combs.append([left, right])
        seen.add(key)

half_combs.sort(key=lambda x: abs(sum(x[0]) - sum(x[1])))
print(int(abs(sum(half_combs[0][1]) - sum(half_combs[0][0]))))
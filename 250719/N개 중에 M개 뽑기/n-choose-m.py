N, M = map(int, input().split())

# Please write your code here.
from itertools import combinations

n_lst = [n for n in range(1, N + 1)]
combs_lst = list(combinations(n_lst, M))

for comb in combs_lst:
    print(*comb)
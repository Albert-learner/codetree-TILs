n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
from itertools import permutations

n_lst = [i for i in range(2, n + 1)]
perms_lst = []
min_cst = sys.maxsize
for perm in permutations(n_lst):
    path = [1] + list(perm) + [1]
    perms_lst.append(path)

perms_pairs_lst = []
for perm_lst in perms_lst:
    perm_pair = [(perm_lst[i], perm_lst[i + 1]) for i in range(len(perm_lst) - 1)]
    perms_pairs_lst.append(perm_pair)

for perm_pair in perms_pairs_lst:
    cost = 0
    for y, x in perm_pair:
        cost += A[y - 1][x - 1]

    min_cst = min(min_cst, cost)

print(min_cst)
n = int(input())

# Please write your code here.
from itertools import permutations

n_lst = [i for i in range(1, n + 1)]
perms_lst = list(permutations(n_lst, n))

for perm in perms_lst:
    print(*perm)
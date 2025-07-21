n = int(input())

# Please write your code here.
from itertools import permutations

n_lst = [i for i in range(1, n + 1)]
perms_lst = sorted(list(permutations(n_lst, len(n_lst))), reverse = True)

for perm in perms_lst:
    print(*perm)

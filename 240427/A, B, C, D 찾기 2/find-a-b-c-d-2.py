from itertools import combinations

num_lst = list(map(int, input().split()))
num_lst.sort()

def possible(x):
    a, b, c, d = x

    if (a + b in num_lst) and (b + c in num_lst) and (c + d in num_lst) and (d + a in num_lst) and \
       (a + c in num_lst) and (b + d in num_lst) and \
       (a + b + c in num_lst) and (a + b + d in num_lst) and (a + c + d in num_lst) and (b + c + d in num_lst) and \
       (a + b + c + d in num_lst):
       return True

    return False

combs_set = set(combinations(num_lst, 4))
for comb in combs_set:
    if possible(comb):
        for num in comb:
            print(num, end = " ")
        break
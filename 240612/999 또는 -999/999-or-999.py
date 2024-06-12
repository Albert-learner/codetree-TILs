n_lst = list(map(int, input().split()))

n_lst = n_lst[:-1]
# print(max(n_lst), min(n_lst))

min_cst, max_cst = n_lst[0], n_lst[0]
for n in n_lst[1:]:
    if n < min_cst:
        min_cst = n
    elif n > max_cst:
        max_cst = n

print(max_cst, min_cst)
N = int(input())
n_lst = list(map(int, input().split()))

min_cst, min_cnts = min(n_lst), 0
for n in n_lst:
    if n == min_cst:
        min_cnts += 1

print(min_cst, min_cnts)

# min_cst, min_cnts = n_lst[0], 0
# for n in n_lst[1:]:
#     if n < min_cst:
#         min_cst = n

# for n in n_lst:
#     if n == min_cst:
#         min_cnts += 1

# print(min_cst, min_cnts)
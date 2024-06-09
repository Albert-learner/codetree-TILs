n_lst = list(map(int, input().split()))

zero_idxs = [idx for idx, n in enumerate(n_lst) if n == 0]
print(sum(n_lst[zero_idxs[0] - 3: zero_idxs[0]]))
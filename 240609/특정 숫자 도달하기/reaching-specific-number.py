n_lst = list(map(int, input().split()))

confirm = False
last_idx = 0
for n in n_lst:
    if n >= 250:
        confirm = True
        last_idx = n_lst.index(n)
        break

if confirm == True:
    print(f"{sum(n_lst[:last_idx])} {sum(n_lst[:last_idx]) / last_idx}")
else:
    print(f"{sum(n_lst)} {sum(n_lst) / 10}")
N = int(input())
n_lst = list(map(int, input().split()))

n_lst_cntr = {n: 0 for n in range(1, 10)}
for n in n_lst:
    if n in n_lst_cntr:
        n_lst_cntr[n] += 1

for n, cnts in n_lst_cntr.items():
    print(cnts)
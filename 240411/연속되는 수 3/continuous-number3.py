N = int(input())
n_lst = [int(input()) for _ in range(N)]

divide_lst, cnts = [], []
for i in range(N):
    if i == 0 or n_lst[i] * n_lst[i - 1] < 0:
        if cnts:
            divide_lst.append(cnts)
        cnts = [n_lst[i]]
    else:
        cnts.append(n_lst[i])

if cnts:
    divide_lst.append(cnts)        

max_cnts = 0
for row in divide_lst:
    if len(row) > max_cnts:
        max_cnts = len(row)

print(max_cnts)
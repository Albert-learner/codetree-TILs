N = int(input())
n_lst = [1, N]

while n_lst[-1] < 100:
    n_lst.append(n_lst[-2] + n_lst[-1])

print(*n_lst)
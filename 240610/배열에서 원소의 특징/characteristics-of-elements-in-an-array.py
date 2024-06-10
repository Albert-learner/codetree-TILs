n_lst = list(map(int, input().split()))

for idx, n in enumerate(n_lst):
    if n % 3 == 0:
        print(n_lst[idx - 1])
        break
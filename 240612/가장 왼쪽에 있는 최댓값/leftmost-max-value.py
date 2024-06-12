N = int(input())
n_lst = list(map(int, input().split()))

while len(n_lst) >= 1:
    max_cst = max(n_lst)

    idx = 0
    for i in range(len(n_lst)):
        if n_lst[i] == max_cst:
            idx = i
            break

    print(idx + 1, end = ' ')
    n_lst = n_lst[:idx]
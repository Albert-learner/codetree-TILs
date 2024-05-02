N = int(input())
n_lst = list(map(int, input().split()))

uniq_n_lst = sorted(list(set(n_lst[:])))

if len(uniq_n_lst) == 1:
    print(-1)
else:
    twos = n_lst.count(uniq_n_lst[1])

    if twos > 1:
        print(-1)
    elif twos == 1:
        print(n_lst.index(uniq_n_lst[1]) + 1)
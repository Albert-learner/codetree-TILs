N = int(input())
n_lst = list(map(int, input().split()))

uniq_n_lst = sorted(list(set(n_lst[:])))
twos = n_lst.count(uniq_n_lst[1])

if twos > 1:
    print(-1)
elif twos == 1:
    print(n_lst.index(uniq_n_lst[1]) + 1)
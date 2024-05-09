N = int(input())
n_lst = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    for j in range(i):
        if n_lst[j] > n_lst[j + 1]:
            n_lst[j], n_lst[j + 1] = n_lst[j + 1], n_lst[j]

print(*n_lst)
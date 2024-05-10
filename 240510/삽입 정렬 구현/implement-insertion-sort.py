N = int(input())
n_lst = list(map(int, input().split()))

for end in range(1, N):
    for i in range(end, 0, -1):
        if n_lst[i - 1] > n_lst[i]:
            n_lst[i - 1], n_lst[i] = n_lst[i], n_lst[i - 1]

print(*n_lst)
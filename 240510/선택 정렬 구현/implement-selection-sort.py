N = int(input())
n_lst = list(map(int, input().split()))

for i in range(len(n_lst) - 1):
    min_idx = i
    for j in range(i + 1, N):
        if n_lst[j] < n_lst[min_idx]:
            min_idx = j

    n_lst[i], n_lst[min_idx] = n_lst[min_idx], n_lst[i]

print(*n_lst)
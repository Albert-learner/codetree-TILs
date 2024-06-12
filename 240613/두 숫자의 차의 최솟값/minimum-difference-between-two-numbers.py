N = int(input())
n_lst = list(map(int, input().split()))

min_diff = n_lst[-1] - n_lst[0]
for i in range(N):
    for j in range(i + 1, N):
        diff = n_lst[j] - n_lst[i]
        if diff < min_diff:
            min_diff = diff

print(min_diff)
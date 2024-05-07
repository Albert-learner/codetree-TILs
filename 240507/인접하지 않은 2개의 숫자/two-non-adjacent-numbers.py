N = int(input())
n_lst = list(map(int, input().split()))

max_sum = 0
for i in range(N):
    for j in range(i + 2, N):
        max_sum = max(max_sum, n_lst[i] + n_lst[j])

print(max_sum)
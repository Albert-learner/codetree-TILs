N = int(input())
n_lst = list(map(int, input().split()))

two_sums = 0
for i in range(N):
    for j in range(i + 2, N):
        if n_lst[i] + n_lst[j] > two_sums:
            two_sums = n_lst[i] + n_lst[j]

print(two_sums)
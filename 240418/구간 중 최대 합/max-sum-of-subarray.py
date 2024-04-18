N, K = map(int, input().split())
n_lst = list(map(int, input().split()))

max_sum = 0
for i in range(N - K + 1):
    max_sum = max(max_sum, sum(n_lst[i:i + K]))

print(max_sum)
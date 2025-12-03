n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
INF = 10 ** 18
best = -INF

for top in range(n):
    col_sum = [0] * n

    for bottom in range(top, n):
        for c in range(n):
            col_sum[c] += arr[bottom][c]

        cur_max = col_sum[0]
        best = max(best, cur_max)
        for c in range(1, n):
            cur_max = max(col_sum[c], cur_max + col_sum[c])
            if cur_max > best:
                best = cur_max

print(best)
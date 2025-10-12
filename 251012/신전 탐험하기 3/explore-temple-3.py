n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp_prev = a[0][:]

for i in range(1, n):
    best1_val, best1_idx, best2_val = -1, -1, -1
    for j in range(m):
        v = dp_prev[j]
        if v > best1_val:
            best2_val = best1_val
            best1_val = v
            best1_idx = j
        elif v > best2_val:
            best2_val = v

    dp_cur = [0] * m
    for j in range(m):
        take = best2_val if j == best1_idx else best1_val
        dp_cur[j] = a[i][j] + take
    dp_prev = dp_cur

print(max(dp_prev))
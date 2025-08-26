n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
W = n - m + 1
best = [[0] * W for _ in range(n)]

for r in range(n):
    row = weight[r]
    for s in range(W):
        seg = row[s:s + m]
        best_val = 0
        for mask in range(1 << m):
            sum_w, sum_v = 0, 0
            for i in range(m):
                if mask & (1 << i):
                    w = seg[i]
                    sum_w += w
                    if sum_w > c:
                        break
                    sum_v += w ** 2
            else:
                if sum_v > best_val:
                    best_val = sum_v

        best[r][s] = best_val

def disjoint(s1, s2):
    return s1 + m <= s2 or s2 + m <= s1

max_sum = 0
for r1 in range(n):
    for s1 in range(W):
        v1 = best[r1][s1]
        for r2 in range(r1, n):
            for s2 in range(W):
                if r1 == r2 and not disjoint(s1, s2):
                    continue
                v2 = best[r2][s2]
                if v1 + v2 > max_sum:
                    max_sum = v1 + v2

print(max_sum)
n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

# Please write your code here.
nums.sort()

len_start = [0] * n
r = 0
for l in range(n):
    if r < l:
        r = l
    while r + 1 < n and nums[r + 1] - nums[l] <= k:
        r += 1
    len_start[l] = r - l + 1

best_end = [0] * n
for i in range(n):
    e = i + len_start[i] - 1
    if len_start[i] > best_end[e]:
        best_end[e] = len_start[i]

prefix_best = [0] * n
for i in range(n):
    if i == 0:
        prefix_best[i] = best_end[i]
    else:
        prefix_best[i] = max(prefix_best[i - 1], best_end[i])

ans = 0
for l in range(n):
    left_best = prefix_best[l - 1] if l > 0 else 0
    ans = max(ans, left_best + len_start[l])

print(ans)
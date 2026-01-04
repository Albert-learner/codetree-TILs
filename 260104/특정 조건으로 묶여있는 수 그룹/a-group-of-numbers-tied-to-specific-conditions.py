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

prefix_best = [0] * n
for i in range(n):
    cur = len_start[i]
    prefix_best[i] = cur if i == 0 else max(prefix_best[i - 1], cur)

ans = 0
for l in range(n):
    best_left = prefix_best[l - 1] if l > 0 else 0
    ans = max(ans, best_left + len_start[l])

print(ans)
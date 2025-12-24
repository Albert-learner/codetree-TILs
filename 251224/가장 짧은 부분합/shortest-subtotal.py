n, s = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
INF = 10 ** 18
ans = INF

cur_sum, l = 0, 0

for r in range(n):
    cur_sum += arr[r]

    while cur_sum >= s:
        ans = min(ans, r - l + 1)
        cur_sum -= arr[l]
        l += 1

print(-1 if ans == INF else ans)
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
cnt, cur_sum, l = 0, 0, 0

for r in range(n):
    cur_sum += arr[r]

    while cur_sum > m and l <= r:
        cur_sum -= arr[l]
        l += 1

    if cur_sum == m:
        cnt += 1
        cur_sum -= arr[l]
        l += 1

print(cnt)
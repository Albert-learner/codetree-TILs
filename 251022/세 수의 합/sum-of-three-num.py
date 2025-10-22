n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
ans = 0
for i in range(n - 2):
    l, r = i + 1, n - 1
    while l < r:
        s = arr[i] + arr[l] + arr[r]
        if s == k:
            ans += 1
            l += 1
        else:
            r -= 1

print(ans)
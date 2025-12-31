n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort()

cnts = 0
l, r = 0, n - 1

while l < r:
    if arr[l] + arr[r] <= k:
        cnts += (r - l)
        l += 1
    else:
        r -= 1

print(cnts)

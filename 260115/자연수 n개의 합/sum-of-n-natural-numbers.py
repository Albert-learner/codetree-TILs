s = int(input())

# Please write your code here.
left, right = 1, 2_000_000_000
ans = 0

while left <= right:
    mid = (left + right) // 2
    total = mid * (mid + 1) // 2
    if total <= s:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
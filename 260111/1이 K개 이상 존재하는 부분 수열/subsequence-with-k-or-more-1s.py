n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
left, cnts_one, ans = 0, 0, n + 1

for right in range(n):
    if arr[right] == 1:
        cnts_one += 1

    while cnts_one >= k:
        ans = min(ans, right - left + 1)
        if arr[left] == 1:
            cnts_one -= 1
        
        left += 1

print(-1 if ans == n + 1 else ans)
n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
seen = set()
l, ans = 0, 0

for r in range(n):
    while arr[r] in seen:
        seen.remove(arr[l])
        l += 1
    seen.add(arr[r])
    ans = max(ans, r - l + 1)

print(ans)

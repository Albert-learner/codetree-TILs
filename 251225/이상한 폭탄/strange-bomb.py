n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
last_pos = {}
ans = -1

for i, x in enumerate(arr):
    if x in last_pos and i - last_pos[x] <= k:
        if x > ans:
            ans = x
    last_pos[x] = i

print(ans)
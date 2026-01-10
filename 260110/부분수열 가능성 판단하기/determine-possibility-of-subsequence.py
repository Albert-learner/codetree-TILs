n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
pref = [n] * m
p = 0
for i in range(m):
    while p < n and A[p] != B[i]:
        p += 1
    if p == n:
        break
    pref[i] = p
    p += 1

suf = [-1] * m
p = n - 1
for i in range(m - 1, -1, -1):
    while p >= 0 and A[p] != B[i]:
        p -= 1
    if p < 0:
        break
    suf[i] = p
    p -= 1

ans = 0
for k in range(m):
    left = pref[k - 1] if k > 0 else -1     
    right = suf[k + 1] if k < m - 1 else n  

    if left == n or right == -1:
        continue

    if left < right:
        ans += 1

print(ans)
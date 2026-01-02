n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a.sort()

l, r = 0, n - 1
best = float("inf")

while l < r:
    s = a[l] + a[r]
    best = min(best, abs(s))

    if s < 0:
        l += 1
    else:
        r -= 1

print(best)
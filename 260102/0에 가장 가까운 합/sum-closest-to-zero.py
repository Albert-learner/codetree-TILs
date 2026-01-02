n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a.sort()

l, r = 0, n - 1
best_sum = float("inf")
best_pair = (a[l], a[r])

while l < r:
    s = a[l] + a[r]
    if abs(s) < abs(best_sum):
        best_sum = s
        best_pair = (a[l], a[r])
        if best_sum == 0:
            break

    if s < 0:
        l += 1
    else:
        r -= 1

print(best_sum)
n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
cur = best = a[0]
for i in range(1, n):
    cur = max(a[i], cur + a[i])
    best = max(best, cur)

print(best)
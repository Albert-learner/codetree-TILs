n, k = map(int, input().split())

mp = {}
for _ in range(n):
    c, p = map(int, input().split())
    mp[p] = mp.get(p, 0) + c

items = sorted(mp.items()) 
positions = [p for p, _ in items]
candies = [c for _, c in items]

l = 0
cur = 0
ans = 0
limit = 2 * k

for r in range(len(items)):
    cur += candies[r]

    while positions[r] - positions[l] > limit:
        cur -= candies[l]
        l += 1

    if cur > ans:
        ans = cur

print(ans)
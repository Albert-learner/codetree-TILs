n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
events = []

for x1, x2 in intervals:
    events.append((x1, 1))
    events.append((x2, -1))

events.sort(key = lambda x: (x[0], x[1]))

cur, ans = 0, 0

for _, d in events:
    cur += d
    if cur > ans:
        ans = cur

print(ans)
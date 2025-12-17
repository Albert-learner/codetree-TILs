n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
events = []
for x1, x2 in intervals:
    events.append((x1, 1))
    events.append((x2 + 1, -1))

events.sort()

cur, ans = 0, 0
for _, delta in events:
    cur += delta
    if cur > ans:
        ans = cur

print(ans)
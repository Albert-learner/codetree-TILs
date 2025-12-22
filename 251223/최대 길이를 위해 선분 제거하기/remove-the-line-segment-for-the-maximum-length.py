n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys

if n == 1:
    print(0)
    sys.exit(0)

events = []
for i, (l, r) in enumerate(segments):
    events.append((l, 1, i))
    events.append((r, 0, i))

events.sort(key=lambda x: (x[0], x[1]))

active = set()
unique = [0] * n
total_union = 0

prev_x = events[0][0]
idx = 0
m = len(events)

while idx < m:
    x = events[idx][0]

    length = x - prev_x
    if length > 0:
        if active:
            total_union += length
            if len(active) == 1:
                only_id = next(iter(active))
                unique[only_id] += length

    while idx < m and events[idx][0] == x:
        _, typ, sid = events[idx]
        if typ == 0:          # end
            active.discard(sid)
        else:                 # start
            active.add(sid)
        idx += 1

    prev_x = x

ans = 0
for i in range(n):
    ans = max(ans, total_union - unique[i])

print(ans)
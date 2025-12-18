N, K = map(int, input().split())
M = []
dir = []

for _ in range(N):
    m, d = input().split()
    M.append(int(m))
    dir.append(d)

# Please write your code here.
events = []
pos = 0  
for m, d in zip(M, dir):
    nxt = pos + m if d == 'R' else pos - m
    l, r = (pos, nxt) if pos < nxt else (nxt, pos)
    events.append((l, 1))   
    events.append((r, -1)) 
    pos = nxt

events.sort()

ans = 0
cnt = 0
prev_x = events[0][0]

i = 0
while i < len(events):
    x = events[i][0]

    if x > prev_x and cnt >= K:
        ans += x - prev_x

    while i < len(events) and events[i][0] == x:
        cnt += events[i][1]
        i += 1

    prev_x = x

print(ans)
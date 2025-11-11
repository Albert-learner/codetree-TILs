n, t = map(int, input().split())
starts = []
speeds = []

for _ in range(n):
    s, v = map(int, input().split())
    starts.append(s)
    speeds.append(v)

# Please write your code here.
groups = 0
curr = None

for i in range(n - 1, -1, -1):
    final_pos = starts[i] + speeds[i] * t
    if curr is None or final_pos < curr:
        groups += 1
        curr = final_pos
    else:
        pass

print(groups)

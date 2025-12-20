n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
p = [interval[0] for interval in intervals]
q = [interval[1] for interval in intervals]

# Please write your code here.
import heapq

jobs = sorted([(p[i], q[i], i) for i in range(n)])

using, free = [], []

ans = [0] * n
next_id = 1

for start, end, idx in jobs:
    while using and using[0][0] <= start:
        _, comp_id = heapq.heappop(using)
        heapq.heappush(free, comp_id)

    if free:
        comp_id = heapq.heappop(free)
    else:
        comp_id = next_id
        next_id += 1

    ans[idx] = comp_id
    heapq.heappush(using, (end, comp_id))

print(*ans)